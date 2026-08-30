from importlib import import_module

__all__ = (
    "generate_enums",
    "generate_errors",
    "generate_methods",
    "generate_responses",
)


def __getattr__(name):
    if name in __all__:
        return import_module(f"{__name__}.{name}").main
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
