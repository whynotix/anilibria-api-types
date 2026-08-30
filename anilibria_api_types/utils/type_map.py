from typing import Optional, Any
from datetime import datetime, date
import uuid
from decimal import Decimal


async def get_type_map(
    openapi_type: Optional[str] = None,
    openapi_format: Optional[str] = None,
    example: Optional[Any] = None,
    schema: Optional[dict] = None,
    enum_classes: Optional[dict] = None,
) -> str:
    """Определяет Python-тип на основе OpenAPI-схемы, формата и примера.

    Args:
        openapi_type: Тип из OpenAPI (string, integer, number, boolean, array, object, null)
        openapi_format: Формат из OpenAPI (date-time, int32, float, uuid, etc.)
        example: Пример значения
        schema: Полная схема (для сложных случаев: enum, array, oneOf, additionalProperties)
        enum_classes: Словарь {кортеж значений enum -> класс enum} для ссылок на сгенерированные enum-классы

    Returns:
        Строка с Python-типом
    """
    if isinstance(schema, dict):
        return await _type_from_schema(schema, enum_classes)

    if openapi_type is None and openapi_format:
        return _type_from_format_only(openapi_format)

    if openapi_type == "string":
        return _map_string_type(openapi_format)

    if openapi_type == "integer":
        return _map_integer_type(openapi_format)

    if openapi_type == "number":
        return _map_number_type(openapi_format)

    if openapi_type == "boolean":
        return "bool"

    if openapi_type == "array":
        return "list"

    if openapi_type == "object":
        return "dict"

    if openapi_type == "null":
        return "None"

    if openapi_type in (None, "any"):
        return _type_from_example(example)

    return _type_from_example(example)


async def _type_from_schema(schema: dict, enum_classes: Optional[dict]) -> str:
    """Определяет Python-тип по полной OpenAPI-схеме."""
    if "enum" in schema:
        enum_class = (enum_classes or {}).get(tuple(schema["enum"]))
        if enum_class:
            return enum_class
        return "int" if schema.get("type") == "integer" else "str"

    for key in ("oneOf", "anyOf"):
        subs = schema.get(key)
        if isinstance(subs, list):
            types = []
            for sub in subs:
                if isinstance(sub, dict):
                    resolved = await get_type_map(schema=sub, enum_classes=enum_classes)
                    if resolved != "Any" and resolved not in types:
                        types.append(resolved)
            if len(types) > 1:
                return "Union[" + ", ".join(types) + "]"
            if len(types) == 1:
                return types[0]
            return "Any"

    subs = schema.get("allOf")
    if isinstance(subs, list):
        for sub in subs:
            if isinstance(sub, dict):
                resolved = await get_type_map(schema=sub, enum_classes=enum_classes)
                if resolved and resolved != "Any":
                    return resolved
        return "Any"

    schema_type = schema.get("type")

    if schema_type == "array":
        items = schema.get("items")
        inner = (
            await get_type_map(schema=items, enum_classes=enum_classes)
            if isinstance(items, dict)
            else "Any"
        )
        return f"list[{inner}]"

    if schema_type == "object":
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            inner = await get_type_map(schema=additional, enum_classes=enum_classes)
            return f"dict[str, {inner}]"
        return "dict"

    if schema_type == "string":
        return _map_string_type(schema.get("format"))

    if schema_type == "integer":
        return "int"

    if schema_type == "number":
        return "float"

    if schema_type == "boolean":
        return "bool"

    if schema_type == "null":
        return "None"

    return "Any"


def _type_from_example(example: Any) -> str:
    """Определяет Python-тип по значению примера"""
    if example is None:
        return "Any"
    elif isinstance(example, str):
        if _is_uuid(example):
            return "uuid.UUID"
        elif _is_datetime(example):
            return "datetime.datetime"
        elif _is_date(example):
            return "datetime.date"
        else:
            return "str"
    elif isinstance(example, bool):
        return "bool"
    elif isinstance(example, int):
        return "int"
    elif isinstance(example, float):
        return "float"
    elif isinstance(example, dict):
        return "dict"
    elif isinstance(example, list):
        return "list"
    elif isinstance(example, (datetime, date)):
        return "datetime.datetime" if isinstance(example, datetime) else "datetime.date"
    elif isinstance(example, uuid.UUID):
        return "uuid.UUID"
    else:
        return f"{type(example).__name__}"


def _type_from_format_only(openapi_format: str) -> str:
    """Определяет тип только по формату"""
    format_mapping = {
        "uuid": "uuid.UUID",
        "date": "datetime.date",
        "date-time": "datetime.datetime",
        "byte": "bytes",
        "binary": "bytes",
        "int32": "int",
        "int64": "int",
        "float": "float",
        "double": "float",
        "decimal": "decimal.Decimal",
        "password": "str",
        "email": "str",
        "uri": "str",
        "hostname": "str",
        "ipv4": "str",
        "ipv6": "str",
        "regex": "str",
    }
    return format_mapping.get(openapi_format, "str")


def _map_string_type(openapi_format: Optional[str]) -> str:
    """Маппинг строковых типов"""
    format_mapping = {
        "byte": "bytes",
        "binary": "bytes",
        "date": "datetime.date",
        "date-time": "datetime.datetime",
        "password": "str",
        "uuid": "uuid.UUID",
        "email": "str",
        "uri": "str",
        "hostname": "str",
        "ipv4": "str",
        "ipv6": "str",
        "regex": "str",
        None: "str"
    }
    return format_mapping.get(openapi_format, "str")


def _map_integer_type(openapi_format: Optional[str]) -> str:
    """Маппинг целочисленных типов"""
    format_mapping = {
        "int32": "int",
        "int64": "int",
        None: "int"
    }
    return format_mapping.get(openapi_format, "int")


def _map_number_type(openapi_format: Optional[str]) -> str:
    """Маппинг числовых типов"""
    format_mapping = {
        "float": "float",
        "double": "float",
        "decimal": "decimal.Decimal",
        None: "float"
    }
    return format_mapping.get(openapi_format, "float")


def _is_uuid(value: str) -> bool:
    """Проверяет, является ли строка UUID"""
    try:
        uuid.UUID(value)
        return True
    except:
        return False


def _is_datetime(value: str) -> bool:
    """Проверяет, является ли строка datetime"""
    try:
        datetime.fromisoformat(value.replace('Z', '+00:00'))
        return True
    except:
        return False


def _is_date(value: str) -> bool:
    """Проверяет, является ли строка date"""
    try:
        date.fromisoformat(value)
        return True
    except:
        return False
