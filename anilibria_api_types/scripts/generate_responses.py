import json
import re
from collections import defaultdict
from pathlib import Path

from anilibria_api_types.config import main_settings
from anilibria_api_types.utils import get_type_map
from anilibria_api_types.validate_schema.get_schema import PATH


def _clean_ident(value: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    if not s or s[0].isdigit():
        s = "_" + s
    return s


def _pascal(ident: str) -> str:
    return "".join(
        part[:1].upper() + part[1:] for part in ident.split("_") if part
    )


def _class_name(name: str) -> str:
    parts = name.split(".")[1:]
    i = 0
    while i < len(parts) and (
        parts[i] == "api" or re.fullmatch(r"v\d+", parts[i])
    ):
        i += 1
    return "".join(part[:1].upper() + part[1:] for part in parts[i:])


def _category(name: str) -> str:
    parts = name.split(".")
    if parts[0] == "commons":
        return "commons"
    rest = parts[1:]
    i = 0
    while i < len(rest) and (
        rest[i] == "api" or re.fullmatch(r"v\d+", rest[i])
    ):
        i += 1
    return rest[i] if i < len(rest) else "misc"


class ResponseBuilder:
    def __init__(self, schemas: dict, class_names: dict) -> None:
        self.schemas = schemas
        self.class_names = class_names
        self.enum_by_values = {}
        self.classes = {}
        self.origin = {}

        for name, schema in schemas.items():
            if (
                name.startswith("enums.")
                and isinstance(schema, dict)
                and "enum" in schema
            ):
                enum_class = class_names[name]
                self.enum_by_values[tuple(schema["enum"])] = enum_class
                self.origin[enum_class] = ("enums", _category(name))

    async def resolve_type(
        self, schema, parent_cls: str, field_hint: str
    ) -> str:
        if not isinstance(schema, dict):
            return "Any"

        if "$ref" in schema:
            ref_name = schema["$ref"].rsplit("/", 1)[-1]
            return self.class_names.get(ref_name, "Any")

        if "enum" in schema:
            enum_class = self.enum_by_values.get(tuple(schema["enum"]))
            if enum_class:
                return enum_class
            return "int" if schema.get("type") == "integer" else "str"

        for key in ("oneOf", "anyOf"):
            subs = schema.get(key)
            if isinstance(subs, list):
                types = []
                for sub in subs:
                    if isinstance(sub, dict):
                        sub_type = await self.resolve_type(
                            sub, parent_cls, field_hint
                        )
                        if sub_type not in types:
                            types.append(sub_type)
                if len(types) > 1:
                    return "Union[" + ", ".join(types) + "]"
                return types[0] if types else "Any"

        if "allOf" in schema and isinstance(schema.get("allOf"), list):
            return await self._declare_composition(
                schema, parent_cls, field_hint
            )

        schema_type = schema.get("type")

        if schema_type == "array":
            items = schema.get("items")
            inner = (
                await self.resolve_type(items, parent_cls, "Item")
                if isinstance(items, dict)
                else "Any"
            )
            return f"list[{inner}]"

        if schema_type == "object":
            if isinstance(schema.get("properties"), dict):
                return await self._declare_object(
                    schema, parent_cls, field_hint
                )
            if isinstance(schema.get("additionalProperties"), dict):
                inner = await self.resolve_type(
                    schema["additionalProperties"], parent_cls, field_hint
                )
                return f"dict[str, {inner}]"
            return "dict"

        return await get_type_map(
            schema=schema, enum_classes=self.enum_by_values
        )

    async def _fill_object_fields(
        self, spec: dict, schema: dict, cls_name: str
    ) -> None:
        seen = {field["name"] for field in spec["fields"]}
        for prop_name, prop_schema in (schema.get("properties") or {}).items():
            field_name = _clean_ident(prop_name)
            if not field_name or field_name in seen:
                continue
            seen.add(field_name)
            field_type = await self.resolve_type(
                prop_schema, cls_name, prop_name
            )
            spec["fields"].append({"name": field_name, "type": field_type})

    async def _declare_object(
        self, schema: dict, parent_cls: str, field_hint: str
    ) -> str:
        name = parent_cls + _pascal(_clean_ident(field_hint))
        if name in self.classes:
            return name
        spec = {"name": name, "kind": "object", "bases": [], "fields": []}
        self.classes[name] = spec
        self.origin[name] = self.origin.get(
            parent_cls, ("responses", self._cls_category(parent_cls))
        )
        await self._fill_object_fields(spec, schema, name)
        return name

    def _cls_category(self, cls_name: str) -> str:
        origin = self.origin.get(cls_name)
        return origin[1] if origin else "misc"

    async def _declare_composition(
        self, schema: dict, parent_cls: str, field_hint: str
    ) -> str:
        name = parent_cls + _pascal(_clean_ident(field_hint))
        if name in self.classes:
            return name
        spec = {"name": name, "kind": "object", "bases": [], "fields": []}
        self.classes[name] = spec
        self.origin[name] = self.origin.get(
            parent_cls, ("responses", self._cls_category(parent_cls))
        )
        for sub in schema.get("allOf") or []:
            if not isinstance(sub, dict):
                continue
            if "$ref" in sub:
                spec["bases"].append(
                    self.class_names.get(
                        sub["$ref"].rsplit("/", 1)[-1], "BaseModel"
                    )
                )
            elif isinstance(sub.get("properties"), dict):
                await self._fill_object_fields(spec, sub, name)
        if isinstance(schema.get("properties"), dict):
            await self._fill_object_fields(spec, schema, name)
        return name

    def _make_spec(self, cls_name: str, category: str) -> dict:
        spec = {"name": cls_name, "category": category}
        self.origin[cls_name] = ("responses", category)
        return spec

    async def build_class(self, name: str, schema: dict) -> dict:
        cls_name = self.class_names[name]
        if cls_name in self.classes:
            return self.classes[cls_name]
        category = _category(name)
        spec = self._make_spec(cls_name, category)
        self.classes[cls_name] = spec

        if not isinstance(schema, dict):
            spec["kind"] = "root"
            spec["root"] = "Any"
            return spec

        if "$ref" in schema:
            spec["kind"] = "root"
            spec["root"] = self.class_names.get(
                schema["$ref"].rsplit("/", 1)[-1], "Any"
            )
            return spec

        if "allOf" in schema and isinstance(schema.get("allOf"), list):
            spec["kind"] = "object"
            spec["bases"] = []
            spec["fields"] = []
            for sub in schema.get("allOf"):
                if not isinstance(sub, dict):
                    continue
                if "$ref" in sub:
                    spec["bases"].append(
                        self.class_names.get(
                            sub["$ref"].rsplit("/", 1)[-1], "BaseModel"
                        )
                    )
                elif isinstance(sub.get("properties"), dict):
                    await self._fill_object_fields(spec, sub, cls_name)
            if isinstance(schema.get("properties"), dict):
                await self._fill_object_fields(spec, schema, cls_name)
            return spec

        schema_type = schema.get("type")
        if schema_type == "object" and isinstance(
            schema.get("properties"), dict
        ):
            spec["kind"] = "object"
            spec["bases"] = []
            spec["fields"] = []
            await self._fill_object_fields(spec, schema, cls_name)
            return spec

        if schema_type is None and ("oneOf" in schema or "anyOf" in schema):
            spec["kind"] = "root"
            spec["root"] = await self.resolve_type(schema, cls_name, name)
            return spec

        spec["kind"] = "root"
        spec["root"] = await self.resolve_type(schema, cls_name, name)
        return spec

    async def build_all(self):
        for name, schema in self.schemas.items():
            if name.startswith("enums."):
                continue
            await self.build_class(name, schema)


def _spec_block(spec: dict) -> str:
    if spec["kind"] == "root":
        return f"class {spec['name']}(RootModel):\n\troot: {spec['root']}\n"
    bases = spec.get("bases") or ["BaseModel"]
    lines = [f"class {spec['name']}({', '.join(bases)}):"]
    if spec["fields"]:
        for field in spec["fields"]:
            field_type = field["type"]
            if field_type == "None":
                lines.append(f"\t{field['name']}: None = None")
            else:
                lines.append(f"\t{field['name']}: {field_type} | None = None")
    else:
        lines.append("\tpass")
    return "\n".join(lines) + "\n"


def _order_specs(specs: list[dict]) -> list[dict]:
    by_name = {s["name"]: s for s in specs}
    visited = {}
    order = []

    def visit(name: str) -> None:
        if name in visited:
            return
        visited[name] = True
        for base in by_name[name].get("bases", []):
            if base in by_name:
                visit(base)
        order.append(by_name[name])

    for name in by_name:
        visit(name)
    return order


def _module_imports(
    specs: list[dict], class_names: dict, origin: dict
) -> list[str]:
    referenced = set()
    stdlib = set()
    typing_names = set()
    type_strings = []
    for spec in specs:
        if spec["kind"] == "object":
            referenced.update(b for b in spec.get("bases") if b != "BaseModel")
            type_strings.extend(field["type"] for field in spec["fields"])
        else:
            type_strings.append(spec["root"])

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
        for cls in class_names.values():
            if re.search(rf"\b{re.escape(cls)}\b", type_str):
                referenced.add(cls)

    lines = [f"import {mod}" for mod in sorted(stdlib)] if stdlib else []
    if typing_names:
        lines.append("from typing import " + ", ".join(sorted(typing_names)))

    by_location = defaultdict(list)
    own = {spec["name"] for spec in specs}
    for cls in referenced:
        if cls in own or cls not in origin:
            continue
        kind, category = origin[cls]
        by_location[(kind, category)].append(cls)

    for kind, category in sorted(by_location):
        names = ", ".join(sorted(by_location[(kind, category)]))
        lines.append(
            f"from anilibria_api_types.codegen.{kind}.{category} import {names}"
        )
    return lines


def _module_text(
    category: str, specs: list[dict], class_names: dict, origin: dict
) -> str:
    specs = _order_specs(specs)
    imports = _module_imports(specs, class_names, origin)
    lines = [
        "# Auto-generated responses/models",
        "from __future__ import annotations",
        "",
        "from pydantic import BaseModel, RootModel",
    ]
    if imports:
        lines.append("")
        lines.extend(imports)
    lines.append("")
    lines.append("")
    for spec in specs:
        lines.append(_spec_block(spec).rstrip("\n"))
        lines.append("")
    return "\n".join(lines) + "\n"


async def generate_responses():
    with open(PATH, encoding="utf-8") as f:
        schema = json.load(f)

    schemas = schema.get("components", {}).get("schemas", {})
    class_names = {name: _class_name(name) for name in schemas}

    builder = ResponseBuilder(schemas, class_names)
    await builder.build_all()

    base_path = Path(f"{main_settings.FOLDER_NAME}/codegen/responses")
    base_path.mkdir(parents=True, exist_ok=True)

    specs = list(builder.classes.values())
    with open(base_path / "models.py", "w", encoding="utf-8") as f:
        f.write(_module_text("models", specs, class_names, builder.origin))


async def main():
    await generate_responses()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
