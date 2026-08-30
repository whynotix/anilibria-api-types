import jsonref
import aiofiles
from pathlib import Path


PATH = Path(__file__).resolve().parent.parent / "temp" / "schema.json"

async def get_schema(path: str = PATH):
    async with aiofiles.open(path, mode="r", encoding="utf-8") as f:
        content = await f.read()
        jsoned = jsonref.loads(content)
        return jsoned


if __name__ == "__main__":
    import asyncio
    asyncio.run(get_schema())