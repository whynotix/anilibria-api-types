# AGENTS.md

Codegen project: generates Pydantic-style method/enum/response/error stubs from the AniLibria OpenAPI schema. Output is committed to `anilibria_api_types/codegen/{methods,enums,errors,responses}/`. **Not a library** — the generated files are the deliverable; run codegen and the diff is the work.

## Setup

- Python `>=3.13`, managed via Poetry (`pyproject.toml`). Use `.venv\Scripts\python.exe`. Run from repo root (no `poetry run`).
- `anilibria_api_types` has **no top-level `__init__.py`** (it's a PEP 420 namespace package). Codegen must be invoked with `-m` from repo root so the repo root lands on `sys.path`.

## Run codegen

```
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_methods
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_enums
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_errors
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_responses
```

- Generators live in `anilibria_api_types/scripts/`, each an independent entrypoint with its own `main()`.
- `anilibria_api_types/main.py` runs the full pipeline (downloads schema, then all four generators) — it needs network. The individual scripts above are the core, repeatable commands.

## Gotchas

- `.env` is required: `config.py` reads `FOLDER_NAME` via pydantic-settings (`env_prefix="MAIN_"` -> `MAIN_FOLDER_NAME`, no default). Codegen crashes without it. See `.env.example`.
- Schema input is `anilibria_api_types/temp/schema.json` (gitignored). Re-download with `validate_schema/download_schema.py` from `https://aniliberty.top/storage/api/docs/v1?aniliberty-api-v1-docs.json`. Schema paths are package-relative via `__file__`, so they don't depend on CWD.
- Type mapping is centralized in `utils/type_map.py:get_type_map` (shared by errors/responses and used by methods indirectly). It resolves nested arrays, `additionalProperties`, `oneOf/allOf`, and enum refs.
- Enum classes are named from the dotted schema path (`enums.anime.releases.release.ageRating` -> `AnimeReleasesReleaseAgeRating`), grouped per category. Errors emit one `ValidationError` for the 422 response; other status codes become `Http<code>Error`.
- Method stubs combine query/path params + request-body props into keyword args (required before optional; path params are required). Same-path operations with multiple HTTP verbs get a `_<verb>` suffix (e.g. `catalog_releases_get`). Each method's `-> <ResponseModel>` comes from the raw, unresolved success response schema. Bodies call the client (`self.api.get/post/delete` with a filtered `params`/`json_data` dict) and parse via `<Model>.model_validate(response)`. Generated files use `from __future__ import annotations` and import referenced enum/response classes.
- Response models go to a SINGLE file `codegen/responses/models.py`, not per-category: the schema's data graph has real cycles (e.g. anime<->accounts), which would circular-import across per-category files. All classes share one module + `from __future__ import annotations`. `generate_responses` reads the schema with raw `json.load` (unresolved `$ref`s). Nested inline objects become sub-models (`<Parent><Field>`); `allOf` becomes inheritance; non-object schemas become `RootModel`.
- Generated method files import `BaseMethod` from `anilibria_api_types.methods.base_method`, which is **not generated and not currently in the repo** — importing the `methods` package fails until a handwritten `base_method.py` is added. `methods/{enums,errors,responses}/__init__.py` just re-export `from anilibria_api_types.codegen.<x> import *`.
- `anilibria-api-client` is a real runtime dependency (`pyproject.toml`).
- Generated files use tabs for indentation.

## Verification

No tests, linter, or typecheck are configured. `.github/workflows/python-publish.yml` builds and publishes to PyPI on a GitHub Release — it never runs codegen or any tests. `.github/workflows/codegen-refresh.yml` runs weekly (and on manual dispatch): it re-downloads the schema, regenerates codegen, and opens a PR with commits limited to `anilibria_api_types/codegen/` whenever the committed generated files change. Verify by running the codegen (the diff against the committed generated files should be expected).
