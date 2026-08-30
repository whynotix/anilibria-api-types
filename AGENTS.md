# AGENTS.md

Codegen project: generates Pydantic-style method stubs from the AniLibria OpenAPI schema (`codegen/methods/*.py`, `codegen/enums/*.py`, `codegen/errors/validation.py`, `codegen/responses/models.py`). Not a library — the committed generated files are the deliverable.

## Setup

- Python >=3.13, managed via Poetry (`pyproject.toml`). Use `.venv\Scripts\python.exe`.
- Run commands from repo root with the venv Python (no `poetry run` needed).

## Run codegen

```
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_methods
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_enums
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_errors
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_responses
```

- Generators live in `anilibria_api_types/scripts/`. Each is an independent entrypoint with its own `main()`. `anilibria_api_types/main.py` is a no-op (its `generate_methods` call is commented out), don't use it.
- Scripts must be run with `-m anilibria_api_types.scripts.<name>` from repo root (they rely on namespace-package resolution).

## Gotchas

- `.env` is required: `config.py` reads `MAIN_FOLDER_NAME` (defaults to nothing, no fallback). Codegen will crash without it. See `.env.example`.
- The schema input lives in `anilibria_api_types/temp/schema.json` (gitignored). Re-download it with `validate_schema/download_schema.py` if missing. Paths are package-relative via `__file__`, so they don't depend on CWD.
- The type-mapping is centralized in `utils/type_map.py:get_type_map` (shared by methods/errors/responses). It takes `schema`, `example`, `enum_classes`, and resolves nested arrays, `additionalProperties`, `oneOf/allOf`, and enum refs.
- Generated output goes to `{FOLDER_NAME}/codegen/{methods,enums,errors,responses}/`. These files are committed — run codegen and the diff is the work.
- Enum classes are named from the dotted schema path (e.g. `enums.anime.releases.release.ageRating` -> `AnimeReleasesReleaseAgeRating`), grouped per category. Errors emit one `ValidationError` for the 422 response.
- Method stubs combine query/path params + request-body props into keyword args (required before optional, path params are required). Same-path operations with multiple HTTP verbs get a `_<verb>` suffix (e.g. `catalog_releases_get`). Each method gets a `-> <ResponseModel>` return annotation resolved from the operation's success response schema (via the raw, unresolved schema), so methods are wired to the generated `codegen/responses` models. Bodies actually call the client: `self.api.get/post/delete` with a filtered `params`/`json_data` dict and parse the result via `<Model>.model_validate(response)`. Generated files use `from __future__ import annotations` and import any referenced enum/response classes, so annotations stay import-safe.
- Responses/models are written to a SINGLE file `codegen/responses/models.py`, not per-category: the schema's data graph has real cycles (e.g. anime<->accounts), which would circular-import across per-category files. All classes share one module + `from __future__ import annotations`, so forward refs resolve lazily. Nested inline objects become sub-models (`<Parent><Field>`); `allOf` becomes inheritance; non-object schemas become `RootModel`.
- `methods/base_method.py` type-hints an external `anilibria_api_client` via `TYPE_CHECKING`; that package is not a dependency.

## Verification

No tests, linter, typecheck, or CI config exist. Verify by running the codegen; generated files use tabs for indentation.
