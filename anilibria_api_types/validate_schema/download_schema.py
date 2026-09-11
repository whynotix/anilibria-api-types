from pathlib import Path

import aiofiles
import aiohttp


async def download_schema(
    url: str = "https://aniliberty.top/storage/api/docs/v1?aniliberty-api-v1-docs.json",
):
    dest = Path(__file__).resolve().parent.parent / "temp" / "schema.json"
    dest.parent.mkdir(parents=True, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                async with aiofiles.open(dest, mode="wb") as file:
                    await file.write(await response.read())


if __name__ == "__main__":
    import asyncio

    asyncio.run(download_schema())
