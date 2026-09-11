import re
from pathlib import Path

from anilibria_api_types.config import main_settings
from anilibria_api_types.utils import get_type_map
from anilibria_api_types.validate_schema.get_schema import get_schema


def _class_name(code: str) -> str:
    return "ValidationError" if code == "422" else f"Http{code}Error"


async def _error_block(code: str, properties: dict) -> str:
    params = []
    for prop_name, prop_details in properties.items():
        prop_type = await get_type_map(schema=prop_details)
        params.append(f"{prop_name}: {prop_type}")
    params_str = (" " + ", ".join(params)) if params else ""

    assign_lines = "\n".join(
        f"\t\tself.{prop_name} = {prop_name}" for prop_name in properties
    )
    init_args = ", ".join(f"self.{prop_name}" for prop_name in properties)
    return (
        f"class {_class_name(code)}(Exception):\n"
        f"\tdef __init__(self,{params_str}) -> None:\n"
        f"{assign_lines}\n"
        f"\t\tsuper().__init__({init_args})\n"
    )


async def generate_errors():
    schema = await get_schema()
    schemas = schema.get("components", {}).get("schemas", {})

    error_schemas = []
    for name, details in schemas.items():
        if not isinstance(details, dict):
            continue
        match = re.match(r"^commons\..*\.responses\.(\d+)\.content$", name)
        if match:
            error_schemas.append((match.group(1), details))

    base_path = Path(f"{main_settings.FOLDER_NAME}/codegen/errors")
    base_path.mkdir(parents=True, exist_ok=True)

    blocks = [
        await _error_block(code, details.get("properties", {}))
        for code, details in error_schemas
    ]

    file_path = base_path / "validation.py"
    content = "# Auto-generated errors\n\n\n" + "\n\n".join(blocks)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


async def main():
    await generate_errors()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
