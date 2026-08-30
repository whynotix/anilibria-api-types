import re
from pathlib import Path

from anilibria_api_types.config import main_settings
from anilibria_api_types.validate_schema.get_schema import get_schema


def _class_name(enum_name: str) -> str:
    segments = enum_name.split(".")[1:]
    return "".join(seg[:1].upper() + seg[1:] for seg in segments)


def _member_name(value) -> str:
    if isinstance(value, str):
        raw = value.upper()
    else:
        raw = f"VALUE_{value}"
    name = re.sub(r"[^A-Z0-9]", "_", raw).strip("_")
    if name and name[0].isdigit():
        name = "_" + name
    return name or "_"


def _base_type(values) -> str:
    if all(isinstance(v, str) for v in values):
        return "str, Enum"
    if all(isinstance(v, int) and not isinstance(v, bool) for v in values):
        return "int, Enum"
    return "Enum"


def _enum_block(enum_name: str, values) -> str:
    lines = [
        f"class {_class_name(enum_name)}({_base_type(values)}):"
    ]
    for value in values:
        repr_value = repr(value) if isinstance(value, str) else str(value)
        lines.append(f"\t{_member_name(value)} = {repr_value}")
    return "\n".join(lines) + "\n"


async def generate_enums():
    schema = await get_schema()
    schemas = schema.get("components", {}).get("schemas", {})

    categories = {}
    for name, details in schemas.items():
        if not isinstance(details, dict):
            continue
        if not name.startswith("enums.") or "enum" not in details:
            continue
        values = details.get("enum")
        if not values:
            continue
        category = name.split(".")[1]
        categories.setdefault(category, [])
        categories[category].append((name, values))

    base_path = Path(f"{main_settings.FOLDER_NAME}/codegen/enums")
    base_path.mkdir(parents=True, exist_ok=True)

    for category, enums in categories.items():
        file_path = base_path / f"{category}.py"
        blocks = []
        for name, values in enums:
            blocks.append(_enum_block(name, values))
        content = (
            f"# Auto-generated for enums in {category} category\n"
            "from enum import Enum\n\n\n"
            + "\n\n".join(blocks)
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)


async def main():
    await generate_enums()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
