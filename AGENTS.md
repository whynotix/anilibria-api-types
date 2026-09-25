# AGENTS.md

Codegen for the AniLibria OpenAPI schema: generates typed method/enum/response/error classes into `anilibria_api_types/codegen/`. Those committed files are the deliverable, so running codegen, applying the ruff pass, and committing the diff is the work. `README.md` covers usage; this file is the agent-specific context.

## Setup

- Python `>=3.13,<4.0.0`, managed via Poetry 2.x (`pyproject.toml`). Dev tooling is in an **optional** `dev` group (`ruff`), so install with `poetry install --with dev`.
- On Windows run generators via `.venv\Scripts\python.exe`; with Poetry use `poetry run python`.
- `anilibria_api_types` has **no top-level `__init__.py`** (PEP 420 namespace package). Always invoke generators with `-m` from the repo root so the repo root is on `sys.path`.
- `.env` with `MAIN_FOLDER_NAME` is required: `config.py` reads `MainSettings.FOLDER_NAME` via pydantic-settings (`env_prefix="MAIN_"`, no default) and codegen crashes without it. See `.env.example`.
- `pyproject.toml` and `poetry.lock` must stay in sync: after editing dependencies/groups run `poetry lock`, otherwise `poetry install` (and CI) fails with "pyproject.toml changed significantly since poetry.lock". The lock must also be current before you can install and regenerate locally.

## Run codegen

```
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_methods
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_enums
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_errors
.venv\Scripts\python.exe -m anilibria_api_types.scripts.generate_responses
```

- Each script in `anilibria_api_types/scripts/` is an independent entrypoint with its own `main()`. There is no `scripts/__init__.py` (it is a PEP 420 namespace subpackage, like the top-level package), so import each by its full module path.
- Full pipeline (downloads the schema, then enums -> errors -> responses -> methods — needs network): `poetry run python -m anilibria_api_types.main`.
- Schema input is `anilibria_api_types/temp/schema.json` (gitignored). Re-download via `validate_schema/download_schema.py`; paths are package-relative (`__file__`), so CWD doesn't matter.

## Regenerating the committed output

The committed `codegen/` is **generator output after a ruff pass**, not the raw generator output. Raw output uses tabs, `Union[...]`, and unsorted/expanded imports; the formatter normalizes it. So after running a generator, always reproduce the CI style step before diffing or committing:

```
poetry run ruff check --fix --unsafe-fixes --exit-zero anilibria_api_types/codegen
poetry run ruff format anilibria_api_types/codegen
```

- Skipping the ruff pass produces a huge spurious diff (every class reformatted) even when the schema did not change.
- Schema changes: run all four generators (or `python -m anilibria_api_types.main`). Generator-logic changes: run the affected generator only.
- Run `git status --short` / `git diff` afterward; an unchanged schema should yield no-op or only the expected diff under `anilibria_api_types/codegen/`.

## Gotchas

- `$ref` handling differs per generator: `get_schema()` runs `jsonref` and ERASES `$ref`s, so `generate_methods` uses resolved `get_schema()` for params but raw `json.load(PATH)` for the success-response `$ref` (return type); `generate_responses` uses raw `json.load`. Do not "simplify" these to one loader.
- Type mapping is centralized in `utils/type_map.py:get_type_map` (schema-first; resolves arrays, `additionalProperties`, `oneOf/anyOf` -> `Union`, `allOf`, and enum refs via the `enum_classes` map). Do not re-implement type logic in generators.
- Method stubs flatten query/path params + request-body props into kwargs (required before optional; path params required). Multi-verb paths get a `_<verb>` suffix (`catalog_releases_get`). Bodies call the client (`self.api.get/post/delete` with a filtered `params`/`json_data` dict) and parse via `<Model>.model_validate(response)`; enum args are unwrapped with `.value` (None-safe for optional query args). Files use `from __future__ import annotations` and import referenced enum/response classes.
- Response models live in a SINGLE `codegen/responses/models.py`, not per-category: the schema graph has real cycles (e.g. anime<->accounts), so per-category files would circular-import. Inline objects become sub-models (`<Parent><Field>`), `allOf` becomes inheritance, non-object schemas become `RootModel`.
- Response models use `from __future__ import annotations`, so every annotation is a string and Pydantic resolves it at runtime. `generate_responses` therefore appends `<Class>.model_rebuild()` for **every** generated model at the end of `models.py`. This is mandatory: models reference classes defined later (e.g. `AnimeCatalogReleases` -> `AnimeCatalogReleasesItem`) and the schema has recursive cycles, so ordering alone cannot fix resolution. Without the rebuild calls, `model_validate` raises `PydanticUserError: ... is not fully defined`. Do not remove the rebuild block.
- `[tool.ruff.lint.flake8-type-checking] runtime-evaluated-base-classes = ["pydantic.BaseModel", "pydantic.RootModel"]` in `pyproject.toml` is **load-bearing**. Without it, `ruff check --unsafe-fixes` moves `import datetime`, `import uuid`, and enum imports into `if TYPE_CHECKING:`, and Pydantic then fails at runtime with `NameError`/`PydanticUndefinedAnnotation` while building the models. Do not remove or narrow this setting.
- `codegen/` has no `__init__.py` either but **is shipped in the wheel**: `[tool.setuptools.packages.find]` includes `anilibria_api_types*` and only excludes `dist*`/`build*`. Do not add `codegen` to `exclude` — generated method bodies import `anilibria_api_types.codegen.*` at runtime, so the package must ship it. The top-level `anilibria_api_types/{methods,enums,errors,responses}/__init__.py` are convenience re-exports of `codegen.*` (and `methods` also re-exports `BaseMethod`).
- `methods/base_method.py` is handwritten (mirrors the client's `BaseMethod`: `self.api = api`); generated method files import it. `anilibria-api-client` is a runtime dependency, so generated bodies assume its `API` (`get/post/delete`).
- Generated files are committed after `ruff format`, so committed codegen uses spaces, not tabs — tabs appear only in raw generator output.

## Verification

- No tests. Lint/format: `poetry run ruff check .` / `poetry run ruff format .` (`ruff` 0.16.8 is a declared optional `dev` dependency; requires `poetry install --with dev`). `[tool.mypy]` config exists, but mypy is NOT declared as a dependency, so `poetry run mypy .` is not reproducible on a fresh install.
- Verify a regeneration by running the generators and importing the generated modules; the expected result is a no-op or an expected diff under `anilibria_api_types/codegen/`.
- Verify model correctness (not just importability) by actually validating a model that exercises forward refs / cycles / special types, e.g. `poetry run python -c "from anilibria_api_types.codegen.responses.models import AnimeCatalogReleases as M; print(M.model_validate({'data': [], 'meta': None}))"`, plus a datetime/uuid field. A real end-to-end check uses `anilibria-api-client` (network): `client.app.status()` and `client.anime.catalog_releases_get(limit=1, include="id")`.

## GitHub automation (`.github/`)

- Branch model: default integration branch is `main`, but all automated PRs target **`dev`** (dependabot, codegen refresh, ruff style). Dependabot is configured with `target-branch: dev`.
- `.github/actions/setup-poetry/action.yml` — shared composite action: setup Python, install Poetry (`virtualenvs-in-project`), cache `.venv` keyed on `poetry.lock`, then `poetry lock` + `poetry install --with dev` on cache miss. Workflows should use `./.github/actions/setup-poetry` instead of repeating setup steps.
- `.github/workflows/codegen-refresh.yml` — weekly (Mon 03:00 UTC) + manual. Checks out `dev`, creates `.env`, sets up via the composite action, runs `python -m anilibria_api_types.main`, applies ruff to `codegen/`, opens a PR (`codegen/refresh`, `add-paths: anilibria_api_types/codegen`, base `dev`). Concurrency group `weekly-codegen-refresh`.
- `.github/workflows/apply-ruff-style.yml` — weekly (Mon 04:00 UTC, staggered after codegen) + manual. Checks out `dev`, applies `ruff check --fix --unsafe-fixes --exit-zero .` + `ruff format .` across the repo, opens a style PR against `dev`. Concurrency group `auto-style-ruff`.
- `.github/workflows/python-publish.yml` — on GitHub Release `published`. Builds with `python -m build` on Python 3.13 and publishes to PyPI via Trusted Publishing (`id-token: write`, `environment: pypi`). Never runs codegen or tests; the published codegen is whatever was committed/merged.
- `.github/workflows/dependabot-automerge-pr.yml` — on `pull_request` (opened/synchronize/reopened) from `dependabot[bot]`, squash-merges and deletes the branch. Concurrency is keyed per PR number. Merges immediately (does not wait for status checks); switch to `gh pr merge --auto` if required checks are added later.
- `.github/dependabot.yml` — daily pip updates (direct only) and weekly `github-actions` updates, both targeting `dev`, max 5 open PRs each.
- `.github/ISSUE_TEMPLATE/` — `bug.yml` and `request.yml` forms.
