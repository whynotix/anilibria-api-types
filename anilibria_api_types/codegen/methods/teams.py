# Auto-generated for methods in teams category
from __future__ import annotations

from typing import Union
from anilibria_api_types.codegen.responses.models import Teams, TeamsRoles, TeamsUsers

from anilibria_api_types.methods.base_method import BaseMethod

class TeamsMethod(BaseMethod):
	async def get(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> Teams:
		"""
		Список команд АниЛибрии
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/teams/", params=params)
		return Teams.model_validate(response)

	async def roles(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> TeamsRoles:
		"""
		Список ролей
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/teams/roles", params=params)
		return TeamsRoles.model_validate(response)

	async def users(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> TeamsUsers:
		"""
		Список анилибрийцов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/teams/users", params=params)
		return TeamsUsers.model_validate(response)

