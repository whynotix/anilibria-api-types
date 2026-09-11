import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from anilibria_api_types.config import main_settings
from anilibria_api_types.utils import get_type_map
from anilibria_api_types.validate_schema.get_schema import PATH, get_schema


def _clean_ident(value: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    if not s or s[0].isdigit():
        s = "_" + s
    return s


def _enum_class_name(enum_name: str) -> str:
    segs = enum_name.split(".")[1:]
    return "".join(seg[:1].upper() + seg[1:] for seg in segs)


def _class_name(schema_name: str) -> str:
    parts = schema_name.split(".")[1:]
    i = 0
    while i < len(parts) and (
        parts[i] == "api" or re.fullmatch(r"v\d+", parts[i])
    ):
        i += 1
    return "".join(part[:1].upper() + part[1:] for part in parts[i:])


def _schema_to_type(schema: dict | None) -> str | None:
    if not isinstance(schema, dict):
        return None
    if "$ref" in schema:
        return _class_name(schema["$ref"].rsplit("/", 1)[-1])
    return None


def _response_return_type(details: dict) -> str | None:
    responses = details.get("responses") or {}

    def schema_for(response: dict) -> dict | None:
        content = (response or {}).get("content") or {}
        for content_details in content.values():
            if isinstance(content_details, dict) and isinstance(
                content_details.get("schema"), dict
            ):
                return content_details["schema"]
        return None

    for code in ("200", "201", "202", "204"):
        if code in responses:
            schema = schema_for(responses[code])
            if schema is not None:
                return _schema_to_type(schema) or None

    for code, response in responses.items():
        if str(code) == "default" or str(code).startswith("2"):
            schema = schema_for(response)
            if schema is not None:
                return _schema_to_type(schema) or None
    return None


def _build_enum_index(schemas: dict) -> tuple[dict, dict]:
    by_values = {}
    by_class = {}
    for name, schema in schemas.items():
        if not isinstance(schema, dict):
            continue
        if name.startswith("enums.") and "enum" in schema:
            values = tuple(schema["enum"])
            if values:
                enum_class = _enum_class_name(name)
                by_values[values] = enum_class
                by_class[enum_class] = name.split(".")[1]
    return by_values, by_class


async def _collect_params(details: dict, enum_classes: dict) -> list[dict]:
    params = []
    seen = set()

    for param in details.get("parameters", []):
        if not isinstance(param, dict) or not param.get("name"):
            continue
        name = _clean_ident(param["name"])
        if not name or name in seen:
            continue
        seen.add(name)
        params.append(
            {
                "name": name,
                "api_name": param["name"],
                "type": await get_type_map(
                    schema=param.get("schema"),
                    example=param.get("example"),
                    enum_classes=enum_classes,
                ),
                "required": bool(
                    param.get("required") or param.get("in") == "path"
                ),
                "origin": param.get("in", "query"),
                "description": param.get("description"),
            }
        )

    request_body = details.get("requestBody")
    if isinstance(request_body, dict):
        content = request_body.get("content") or {}
        for content_details in content.values():
            schema = (content_details or {}).get("schema") or {}
            required_props = set(schema.get("required") or [])
            for prop_name, prop_schema in (
                schema.get("properties") or {}
            ).items():
                name = _clean_ident(prop_name)
                if not name or name in seen:
                    continue
                seen.add(name)
                params.append(
                    {
                        "name": name,
                        "api_name": prop_name,
                        "type": await get_type_map(
                            schema=prop_schema,
                            enum_classes=enum_classes,
                        ),
                        "required": prop_name in required_props,
                        "origin": "body",
                        "description": prop_schema.get("description")
                        if isinstance(prop_schema, dict)
                        else None,
                    }
                )

    return params


def _ordered_params(params: list[dict]) -> list[dict]:
    required = [p for p in params if p["required"]]
    optional = [p for p in params if not p["required"]]
    return required + optional


def _build_url(
    path: str, path_params: list[dict], enum_classes: set[str]
) -> str:
    if not path_params:
        return f'"{path}"'

    value_map = {
        param["name"]: _path_value(param["name"], param["type"], enum_classes)
        for param in path_params
    }

    def replace(match: re.Match) -> str:
        cleaned = _clean_ident(match.group(1))
        return "{" + value_map.get(cleaned, cleaned) + "}"

    cleaned = re.sub(r"\{([^}]+)\}", replace, path)
    return f'f"{cleaned}"'


def _path_value(name: str, type_str: str, enum_classes: set[str]) -> str:
    if type_str in enum_classes:
        return f"{name}.value"
    return name


def _query_value(name: str, type_str: str, enum_classes: set[str]) -> str:
    if type_str in enum_classes:
        return f"({name}.value if {name} is not None else None)"
    list_match = re.fullmatch(r"list\[([A-Za-z_][A-Za-z0-9_]*)\]", type_str)
    if list_match and list_match.group(1) in enum_classes:
        return f"([v.value for v in {name}] if {name} is not None else None)"
    return name


def _method_docstring(params: list[dict], summary: str | None) -> str | None:
    lines = []
    if summary:
        lines.append(summary)
    for param in params:
        if param.get("description"):
            lines.append(f":param {param['name']}: {param['description']}")
    if not lines:
        return None
    return '\t\t"""\n\t\t' + "\n\t\t".join(lines) + '\n\t\t"""'


def _method_body(
    verb: str,
    path: str,
    params: list[dict],
    return_type: str | None,
    enum_classes: set[str],
) -> list[str]:
    indent = "\t\t"
    lines = []

    query_params = [p for p in params if p["origin"] == "query"]
    body_params = [p for p in params if p["origin"] == "body"]

    if query_params:
        items = ", ".join(
            f'"{p["api_name"]}": {_query_value(p["name"], p["type"], enum_classes)}'
            for p in query_params
        )
        lines.append(
            f"{indent}params = {{k: v for k, v in {{{items}}}.items() if v is not None}}"
        )
    if body_params:
        items = ", ".join(
            f'"{p["api_name"]}": {p["name"]}' for p in body_params
        )
        lines.append(f"{indent}data = {{{items}}}")

    url = _build_url(
        path, [p for p in params if p["origin"] == "path"], enum_classes
    )

    if verb in ("get", "post", "delete"):
        fn = verb
        prelude = None
        call_args = []
        if verb == "get" and query_params:
            call_args.append("params=params")
        elif verb in ("post", "delete") and body_params:
            call_args.append("json_data=data")
    else:
        fn = "request"
        prelude = f'"{verb.upper()}"'
        call_args = []
        if query_params:
            call_args.append("params=params")
        if body_params:
            call_args.append("json_data=data")

    if prelude is None:
        call = f"await self.api.{fn}({url}"
    else:
        call = f"await self.api.{fn}({prelude}, {url}"
    if call_args:
        call += ", " + ", ".join(call_args)
    call += ")"

    if return_type:
        lines.append(f"{indent}response = {call}")
        lines.append(f"{indent}return {return_type}.model_validate(response)")
    else:
        lines.append(f"{indent}return {call}")
    return lines


def _method_code(
    method: dict,
    enum_classes: set[str],
) -> str:
    name = method["name"]
    params = method["params"]
    ordered = _ordered_params(params)
    annotation = (
        f" -> {method['return_type']}" if method.get("return_type") else ""
    )
    lines = [f"\tasync def {name}(", "\t\tself,"]
    for i, param in enumerate(ordered):
        decl = f"\t\t{param['name']}: {param['type']}"
        if not param["required"]:
            decl += " | None = None"
        lines.append(decl + ("," if i < len(ordered) - 1 else ""))
    lines.append(f"\t){annotation}:")

    docstring = _method_docstring(ordered, method.get("summary"))
    if docstring:
        lines.append(docstring)

    lines.extend(
        _method_body(
            method["verb"],
            method["path"],
            ordered,
            method.get("return_type"),
            enum_classes,
        )
    )
    return "\n".join(lines) + "\n"


def _method_name_from_path(path: str) -> str:
    segments = [s for s in path.strip("/").split("/") if s]
    if len(segments) <= 1:
        return "get"
    cleaned = [_clean_ident(s) for s in segments[1:]]
    cleaned = [c for c in cleaned if c]
    return "_".join(cleaned) if cleaned else "get"


def _category_imports(
    methods: list[dict], enum_by_class: dict, class_names: list[str]
) -> list[str]:
    enum_references = defaultdict(set)
    response_references = set()
    stdlib = set()
    typing_names = set()

    for method in methods:
        type_strings = [param["type"] for param in method["params"]]
        if method.get("return_type"):
            type_strings.append(method["return_type"])
        for type_str in type_strings:
            stdlib |= {
                mod
                for mod in ("datetime", "uuid", "decimal")
                if mod + "." in type_str
            }
            typing_names |= {
                name
                for name in ("Union", "Any")
                if re.search(rf"\b{name}\b", type_str)
            }
            for cls in class_names:
                if re.search(rf"\b{re.escape(cls)}\b", type_str):
                    if cls in enum_by_class:
                        enum_references[enum_by_class[cls]].add(cls)
                    else:
                        response_references.add(cls)

    lines = [f"import {module}" for module in sorted(stdlib)] if stdlib else []
    if typing_names:
        lines.append("from typing import " + ", ".join(sorted(typing_names)))
    for category in sorted(enum_references):
        names = ", ".join(sorted(enum_references[category]))
        lines.append(
            f"from anilibria_api_types.codegen.enums.{category} import {names}"
        )
    if response_references:
        names = ", ".join(sorted(response_references))
        lines.append(
            f"from anilibria_api_types.codegen.responses.models import {names}"
        )
    return lines


def _category_file(
    category: str,
    methods: list[dict],
    enum_by_class: dict,
    class_names: list[str],
) -> str:
    category_imports = _category_imports(methods, enum_by_class, class_names)
    lines = [
        f"# Auto-generated for methods in {category} category",
        "from __future__ import annotations",
        "",
    ]
    lines.extend(category_imports)
    if category_imports:
        lines.append("")
    lines.extend(
        [
            "from anilibria_api_types.methods.base_method import BaseMethod",
            "",
            f"class {category.capitalize()}Method(BaseMethod):",
        ]
    )
    for method in methods:
        lines.append(_method_code(method, set(enum_by_class)).rstrip("\n"))
        lines.append("")
    return "\n".join(lines) + "\n"


async def generate_methods():
    schema = await get_schema()
    with open(PATH, encoding="utf-8") as f:
        raw_schema = json.load(f)
    raw_paths = raw_schema.get("paths", {})
    paths = schema.get("paths", {})
    enum_by_values, enum_by_class = _build_enum_index(
        schema.get("components", {}).get("schemas", {})
    )
    class_names = [
        _class_name(name)
        for name in schema.get("components", {}).get("schemas", {})
    ]

    operations = []
    for path, methods_dict in paths.items():
        if not isinstance(methods_dict, dict):
            continue
        category = _clean_ident(path.strip("/").split("/")[0])
        for verb, details in methods_dict.items():
            if not isinstance(details, dict):
                continue
            raw_details = raw_paths.get(path, {}).get(verb, {})
            operations.append(
                {
                    "category": category,
                    "base_name": _method_name_from_path(path),
                    "verb": verb,
                    "path": path,
                    "summary": details.get("summary"),
                    "params": await _collect_params(details, enum_by_values),
                    "return_type": _response_return_type(raw_details),
                }
            )

    verb_counts = Counter(
        (op["category"], op["base_name"]) for op in operations
    )

    methods_by_category = defaultdict(list)
    for op in operations:
        name = op["base_name"]
        if verb_counts[(op["category"], op["base_name"])] > 1:
            name = f"{name}_{op['verb']}"
        op["name"] = name
        methods_by_category[op["category"]].append(op)

    base_path = Path(f"{main_settings.FOLDER_NAME}/codegen/methods")
    base_path.mkdir(parents=True, exist_ok=True)

    for category, methods in methods_by_category.items():
        methods.sort(key=lambda m: m["name"])
        with open(base_path / f"{category}.py", "w", encoding="utf-8") as f:
            f.write(
                _category_file(category, methods, enum_by_class, class_names)
            )


async def main():
    await generate_methods()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
