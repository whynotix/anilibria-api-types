# anilibria-api-types

RU | [EN](https://github.com/whynotix/anilibria-api-types/tree/main/README.md)

[![pypi](https://img.shields.io/pypi/v/anilibria-api-types.svg)](https://pypi.org/project/anilibria-api-types/) [![license](https://img.shields.io/github/license/whynotix/anilibria-api-types
)](https://github.com/whynotix/anilibria-api-types/blob/main/LICENSE)



Типизированные Pydantic-стабы для **AniLibria API** — классы методов, enum-ов, ответов и ошибок, генерируемые из [OpenAPI-схемы](https://aniliberty.top/storage/api/docs/v1?aniliberty-api-v1-docs.json). Закоммиченные файлы в `anilibria_api_types/codegen/` и есть результат работы, поэтому запуск codegen и коммит diff - и есть суть задачи.

## Требования

- Python `>=3.13` (через [Poetry](https://python-poetry.org/)).
- `.env` с `MAIN_FOLDER_NAME` (см. `.env.example`); `anilibria_api_types/config.py` читает его и падает без него.

## Запуск codegen

```bash
python -m anilibria_api_types.scripts.generate_methods
python -m anilibria_api_types.scripts.generate_enums
python -m anilibria_api_types.scripts.generate_errors
python -m anilibria_api_types.scripts.generate_responses
```

В Windows с Poetry-окружением добавьте префикс `.venv\Scripts\python.exe`. Пакет является namespace-пакетом PEP 420, поэтому запускайте через `-m` из корня репозитория.

Или запустите весь конвейер (загрузит схему, затем запустит все четыре генератора — нужна сеть):

```bash
python -m anilibria_api_types.main
```

Каждый генератор пишет в `anilibria_api_types/codegen/{methods,enums,errors,responses}/`. Схема кэшируется в `anilibria_api_types/temp/schema.json` (gitignored); заново скачать её можно через `validate_schema/download_schema.py`.

## Как это работает

- Каждый генератор — независимая точка входа в `anilibria_api_types/scripts/`.
- Маппинг типов централизован в `anilibria_api_types/utils/type_map.py:get_type_map`.
- Enum-классы именуются по точечному пути схемы (например, `enums.anime.releases.release.ageRating` → `AnimeReleasesReleaseAgeRating`), сгруппированы по категориям.
- Модели ответов находятся в одном файле, `anilibria_api_types/codegen/responses/models.py`, потому что в графе данных схемы есть циклы.
- Сгенерированные классы методов импортируют написанный вручную `BaseMethod` из `anilibria_api_types.methods.base_method`.

## CI

- `.github/workflows/codegen-refresh.yml` (еженедельно): перегенерирует codegen и открывает PR, если закоммиченные файлы изменились.
- `.github/workflows/python-publish.yml` (release): собирает и публикует на PyPI.

## Лицензия

Лицензировано под [The Unlicense](https://unlicense.org/).
