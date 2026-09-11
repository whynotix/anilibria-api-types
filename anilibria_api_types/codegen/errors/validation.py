# Auto-generated errors


class ValidationError(Exception):
    def __init__(self, errors: dict[str, list[str]]) -> None:
        self.errors = errors
        super().__init__(self.errors)
