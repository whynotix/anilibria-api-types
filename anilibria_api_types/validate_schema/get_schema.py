from pathlib import Path

import aiofiles
import jsonref


PATH = Path(__file__).resolve().parent.parent / "temp" / "schema.json"


async def get_schema(path: str = PATH):
    async with aiofiles.open(path, encoding="utf-8") as f:
        content = await f.read()
        return jsonref.loads(content)


if __name__ == "__main__":
    import asyncio

    asyncio.run(get_schema())
