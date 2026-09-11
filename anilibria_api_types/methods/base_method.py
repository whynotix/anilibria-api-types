from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from anilibria_api_client.base_api.api_class import API


class BaseMethod:
    def __init__(self, api: "API") -> None:
        self.api = api
