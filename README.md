# anilibria-api-types

[RU](https://github.com/whynotix/anilibria-api-types/tree/main/.github/README.ru_RU.md) | EN

[![pypi](https://img.shields.io/pypi/v/anilibria-api-types.svg)](https://pypi.org/project/anilibria-api-types/)

Typed Pydantic-style stubs for the **AniLibria API** — method, enum, response, and error classes generated from the [OpenAPI schema](https://aniliberty.top/storage/api/docs/v1?aniliberty-api-v1-docs.json). The committed files under `anilibria_api_types/codegen/` are the deliverable, so running codegen and committing the diff is the work.

## Setup

- Python `>=3.13` (via [Poetry](https://python-poetry.org/)).
- `.env` with `MAIN_FOLDER_NAME` (see `.env.example`); `anilibria_api_types/config.py` reads it and fails without it.

## Run codegen

```bash
python -m anilibria_api_types.scripts.generate_methods
python -m anilibria_api_types.scripts.generate_enums
python -m anilibria_api_types.scripts.generate_errors
python -m anilibria_api_types.scripts.generate_responses
```

On Windows with the Poetry venv, prefix with `.venv\Scripts\python.exe`. The package is a PEP 420 namespace package, so run with `-m` from the repo root.

Run the whole pipeline (downloads the schema, then all four generators — requires network):

```bash
python -m anilibria_api_types.main
```

Each generator writes to `anilibria_api_types/codegen/{methods,enums,errors,responses}/`. The schema is cached at `anilibria_api_types/temp/schema.json` (gitignored); re-download it via `validate_schema/download_schema.py`.

## How it works

- Each generator is an independent entrypoint in `anilibria_api_types/scripts/`.
- Type mapping is centralized in `anilibria_api_types/utils/type_map.py:get_type_map`.
- Enum classes are named from the dotted schema path (e.g. `enums.anime.releases.release.ageRating` → `AnimeReleasesReleaseAgeRating`), grouped per category.
- Response models share a single file, `anilibria_api_types/codegen/responses/models.py`, because the schema's data graph has cycles.
- Generated method classes import a handwritten `BaseMethod` from `anilibria_api_types.methods.base_method`.

## CI

- `.github/workflows/codegen-refresh.yml` (weekly): regenerates codegen and opens a PR if the committed files change.
- `.github/workflows/python-publish.yml` (release): builds and publishes to PyPI.

## License

Licensed under [The Unlicense](https://unlicense.org/).
