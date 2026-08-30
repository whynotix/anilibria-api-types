# Auto-generated for methods in app category
from __future__ import annotations

from typing import Union
from anilibria_api_types.codegen.responses.models import AppSearchReleases, AppStatus

from anilibria_api_types.methods.base_method import BaseMethod

class AppMethod(BaseMethod):
	async def search_releases(
		self,
		query: str,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AppSearchReleases:
		"""
		Поиск релизов
		:param query: Поисковая строка
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"query": query, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/app/search/releases", params=params)
		return AppSearchReleases.model_validate(response)

	async def status(
		self,
	) -> AppStatus:
		"""
		Статус API
		"""
		response = await self.api.get("/app/status")
		return AppStatus.model_validate(response)

