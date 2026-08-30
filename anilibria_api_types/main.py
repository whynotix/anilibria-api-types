from anilibria_api_types.scripts import generate_responses, generate_methods, generate_errors, generate_enums
from anilibria_api_types.validate_schema import download_schema
            
async def main():
    print("Starting download schema...")
    await download_schema()
    print("Schema downloaded, starting create codegen...")
    await generate_enums()
    await generate_errors()
    await generate_responses()
    await generate_methods()
    print("Codegen generated, alldone")
    


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())