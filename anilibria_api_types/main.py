from anilibria_api_types.scripts.generate_enums import main as generate_enums
from anilibria_api_types.scripts.generate_errors import main as generate_errors
from anilibria_api_types.scripts.generate_methods import (
    main as generate_methods,
)
from anilibria_api_types.scripts.generate_responses import (
    main as generate_responses,
)
from anilibria_api_types.validate_schema import download_schema


async def main():
    await download_schema()
    await generate_enums()
    await generate_errors()
    await generate_responses()
    await generate_methods()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
