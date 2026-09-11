# AGENTS.md

Codegen for the AniLibria OpenAPI schema: generates typed method/enum/response/error classes into `anilibria_api_types/codegen/`. Those committed files are the deliverable, so running codegen and committing the diff is the work. `README.md` covers usage; this file is the agent-specific context.

## Setup

- Python `>=3.13`, managed via Poetry (`pyproject.toml`). Dev tooling is in an **optional** `dev` group (`ruff`), so install with `poetry install --with dev`. Generators run from the repo root via `.venv\Scripts\python.exe` (or `poetry run python`).
- `anilibria_api_types` has **no top-level `__init__.py`** (PEP 420 namespace package). Always invoke generators with `-m` from the repo root so the repo root is on `sys.path`.
- `.env` with `MAIN_FOLDER_NAME` is required: `config.py` uses pydantic-settings (`env_prefix="MAIN_"`, no default) and codegen crashes without it. See `.env.example`.

## Run codegen

```
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_methods
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_enums
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_errors
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_responses
```

- Each script in `anilibria_api_types/scripts/` is an independent entrypoint with its own `main()`. `scripts/__init__.py` lazy-loads them (no eager import side effects).
- Full pipeline (downloads the schema, then all four — needs network): `python -m anilibria_api_types.main`.
- Schema input is `anilibria_api_types/temp/schema.json` (gitignored). Re-download via `validate_schema/download_schema.py`; paths are package-relative (`__file__`), so CWD doesn't matter.

## Gotchas

- `$ref` handling differs per generator: `get_schema()` runs `jsonref` and ERASES `$ref`s, so `generate_methods` uses resolved `get_schema()` for params but raw `json.load(PATH)` for the success-response `$ref` (return type); `generate_responses` uses raw `json.load`. Do not "simplify" these to one loader.
- Type mapping is centralized in `utils/type_map.py:get_type_map` (schema-first; resolves arrays, `additionalProperties`, `oneOf/anyOf` -> `Union`, `allOf`, and enum refs via the `enum_classes` map). Do not re-implement type logic in generators.
- Method stubs flatten query/path params + request-body props into kwargs (required before optional; path params required). Multi-verb paths get a `_<verb>` suffix (`catalog_releases_get`). Bodies call the client (`self.api.get/post/delete` with a filtered `params`/`json_data` dict) and parse via `<Model>.model_validate(response)`; enum args are unwrapped with `.value` (None-safe for optional query args). Files use `from __future__ import annotations` and import referenced enum/response classes.
- Response models live in a SINGLE `codegen/responses/models.py`, not per-category: the schema graph has real cycles (e.g. anime<->accounts), so per-category files would circular-import. Inline objects become sub-models (`<Parent><Field>`), `allOf` becomes inheritance, non-object schemas become `RootModel`.
- `codegen/` is excluded from the built package (`[tool.setuptools.packages.find] exclude`). The top-level `anilibria_api_types/{methods,enums,errors,responses}/__init__.py` are convenience re-exports of `codegen.*` (and `methods` also re-exports `BaseMethod`).
- `methods/base_method.py` is handwritten (mirrors the client's `BaseMethod`: `self.api = api`); generated method files import it. `anilibria-api-client` is a runtime dependency, so generated bodies assume its `API` (`get/post/delete`).
- `pyproject.toml` and `poetry.lock` must stay in sync: after editing dependencies/groups run `poetry lock`, otherwise `poetry install` (and CI) fails with "pyproject.toml changed significantly since poetry.lock".
- Generated files use tabs for indentation.

## Verification

- No tests. Lint/format: `poetry run ruff check .` / `poetry run ruff format .` (`ruff` 0.16.1 is a declared optional `dev` dependency; requires `poetry install --with dev`). `[tool.mypy]` config exists, but mypy is NOT declared as a dependency, so `poetry run mypy .` is not reproducible on a fresh install.
- Verify by running the generators and importing the generated modules; the expected result is a no-op or an expected diff under `anilibria_api_types/codegen/`.
- CI: `.github/workflows/apply-ruff-style.yml` (weekly) runs ruff over the whole repo and opens a style PR; `.github/workflows/codegen-refresh.yml` (weekly) regenerates codegen, runs ruff over `anilibria_api_types/codegen`, and opens a PR limited to that path; `.github/workflows/python-publish.yml` builds/publishes to PyPI on a GitHub Release (never runs codegen or tests).
