# Auto-generated for methods in accounts category
from __future__ import annotations

import datetime
from typing import Union
from anilibria_api_types.codegen.enums.accounts import AccountsUsersUserCollectionType, AccountsUsersUserFavoriteFilterSorting, AccountsUsersUserSocialType
from anilibria_api_types.codegen.enums.anime import AnimeReleasesReleaseAgeRating, AnimeReleasesReleaseType
from anilibria_api_types.codegen.responses.models import AccountsOtpGet, AccountsOtpLogin, AccountsUsersAuthLogin, AccountsUsersAuthLogout, AccountsUsersAuthSocialAuthenticate, AccountsUsersAuthSocialLogin, AccountsUsersCollectionsReleases, AccountsUsersMeCollectionsReferencesAgeRatings, AccountsUsersMeCollectionsReferencesGenres, AccountsUsersMeCollectionsReferencesTypes, AccountsUsersMeCollectionsReferencesYears, AccountsUsersMeFavoritesDelete, AccountsUsersMeFavoritesIds, AccountsUsersMeFavoritesReferencesAgeRatings, AccountsUsersMeFavoritesReferencesGenres, AccountsUsersMeFavoritesReferencesSorting, AccountsUsersMeFavoritesReferencesTypes, AccountsUsersMeFavoritesReferencesYears, AccountsUsersMeFavoritesReleases, AccountsUsersMeFavoritesUpdate, AccountsUsersMeViewsHistory, UsersV1User

from anilibria_api_types.methods.base_method import BaseMethod

class AccountsMethod(BaseMethod):
	async def otp_accept(
		self,
		code: int
	):
		"""
		Присоединяем пользователя к выданному OTP
		"""
		data = {"code": code}
		return await self.api.post("/accounts/otp/accept", json_data=data)

	async def otp_get(
		self,
		device_id: str
	) -> AccountsOtpGet:
		"""
		Запрашивает OTP
		"""
		data = {"device_id": device_id}
		response = await self.api.post("/accounts/otp/get", json_data=data)
		return AccountsOtpGet.model_validate(response)

	async def otp_login(
		self,
		code: int,
		device_id: str
	) -> AccountsOtpLogin:
		"""
		Авторизуемся по OTP
		"""
		data = {"code": code, "device_id": device_id}
		response = await self.api.post("/accounts/otp/login", json_data=data)
		return AccountsOtpLogin.model_validate(response)

	async def users_auth_login(
		self,
		login: str,
		password: str
	) -> AccountsUsersAuthLogin:
		"""
		Авторизация пользователя
		"""
		data = {"login": login, "password": password}
		response = await self.api.post("/accounts/users/auth/login", json_data=data)
		return AccountsUsersAuthLogin.model_validate(response)

	async def users_auth_logout(
		self,
	) -> AccountsUsersAuthLogout:
		"""
		Деавторизация пользователя
		"""
		response = await self.api.post("/accounts/users/auth/logout")
		return AccountsUsersAuthLogout.model_validate(response)

	async def users_auth_password_forget(
		self,
		email: str
	):
		"""
		Восстановление пароля
		"""
		data = {"email": email}
		return await self.api.post("/accounts/users/auth/password/forget", json_data=data)

	async def users_auth_password_reset(
		self,
		token: str,
		password: str,
		password_confirmation: str
	):
		"""
		Сброс и установка нового пароля
		"""
		data = {"token": token, "password": password, "password_confirmation": password_confirmation}
		return await self.api.post("/accounts/users/auth/password/reset", json_data=data)

	async def users_auth_social_authenticate(
		self,
		state: str
	) -> AccountsUsersAuthSocialAuthenticate:
		"""
		Аутентифицировать пользователя через социальные сети
		:param state: Ключ аутентификации
		"""
		params = {k: v for k, v in {"state": state}.items() if v is not None}
		response = await self.api.get("/accounts/users/auth/social/authenticate", params=params)
		return AccountsUsersAuthSocialAuthenticate.model_validate(response)

	async def users_auth_social_provider_login(
		self,
		provider: AccountsUsersUserSocialType
	) -> AccountsUsersAuthSocialLogin:
		"""
		Авторизация пользователя через социальные сети
		:param provider: Провайдер социальной сети
		"""
		response = await self.api.get(f"/accounts/users/auth/social/{provider.value}/login")
		return AccountsUsersAuthSocialLogin.model_validate(response)

	async def users_me_collections_delete(
		self,
	):
		"""
		Удалить релизы из коллекций
		"""
		return await self.api.delete("/accounts/users/me/collections")

	async def users_me_collections_ids(
		self,
	):
		"""
		Список идентификаторов релизов добавленных в коллекции
		"""
		return await self.api.get("/accounts/users/me/collections/ids")

	async def users_me_collections_post(
		self,
	):
		"""
		Добавить релизы в коллекции
		"""
		return await self.api.post("/accounts/users/me/collections")

	async def users_me_collections_references_age_ratings(
		self,
	) -> AccountsUsersMeCollectionsReferencesAgeRatings:
		"""
		Список возрастных рейтингов в коллекциях пользователя
		"""
		response = await self.api.get("/accounts/users/me/collections/references/age-ratings")
		return AccountsUsersMeCollectionsReferencesAgeRatings.model_validate(response)

	async def users_me_collections_references_genres(
		self,
	) -> AccountsUsersMeCollectionsReferencesGenres:
		"""
		Список жанров в коллекциях пользователя
		"""
		response = await self.api.get("/accounts/users/me/collections/references/genres")
		return AccountsUsersMeCollectionsReferencesGenres.model_validate(response)

	async def users_me_collections_references_types(
		self,
	) -> AccountsUsersMeCollectionsReferencesTypes:
		"""
		Список типов в коллекциях пользователя
		"""
		response = await self.api.get("/accounts/users/me/collections/references/types")
		return AccountsUsersMeCollectionsReferencesTypes.model_validate(response)

	async def users_me_collections_references_years(
		self,
	) -> AccountsUsersMeCollectionsReferencesYears:
		"""
		Список годов в коллекциях пользователя
		"""
		response = await self.api.get("/accounts/users/me/collections/references/years")
		return AccountsUsersMeCollectionsReferencesYears.model_validate(response)

	async def users_me_collections_releases_get(
		self,
		type_of_collection: AccountsUsersUserCollectionType,
		page: int | None = None,
		limit: int | None = None,
		f_genres: str | None = None,
		f_types: list[AnimeReleasesReleaseType] | None = None,
		f_years: str | None = None,
		f_search: str | None = None,
		f_age_ratings: list[AnimeReleasesReleaseAgeRating] | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AccountsUsersCollectionsReleases:
		"""
		Список релизов добавленных в коллекцию [GET]
		:param type_of_collection: Тип коллекции
		:param page: Номер страницы
		:param limit: Ограничение на количество элементов
		:param f_genres: Список идентификаторов жанров
		:param f_types: Список типов релизов
		:param f_years: Минимальный год выхода релиза
		:param f_search: Поисковый запрос
		:param f_age_ratings: Список возрастных рейтингов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"type_of_collection": (type_of_collection.value if type_of_collection is not None else None), "page": page, "limit": limit, "f[genres]": f_genres, "f[types]": ([v.value for v in f_types] if f_types is not None else None), "f[years]": f_years, "f[search]": f_search, "f[age_ratings]": ([v.value for v in f_age_ratings] if f_age_ratings is not None else None), "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/accounts/users/me/collections/releases", params=params)
		return AccountsUsersCollectionsReleases.model_validate(response)

	async def users_me_collections_releases_post(
		self,
		page: int | None = None,
		limit: int | None = None,
		type_of_collection: AccountsUsersUserCollectionType | None = None,
		f: dict | None = None,
		include: str | None = None,
		exclude: str | None = None
	) -> AccountsUsersCollectionsReleases:
		"""
		Список релизов добавленных в коллекцию [POST]
		:param type_of_collection: Тип коллекции
		"""
		data = {"page": page, "limit": limit, "type_of_collection": type_of_collection, "f": f, "include": include, "exclude": exclude}
		response = await self.api.post("/accounts/users/me/collections/releases", json_data=data)
		return AccountsUsersCollectionsReleases.model_validate(response)

	async def users_me_favorites_delete(
		self,
	) -> AccountsUsersMeFavoritesDelete:
		"""
		Удалить релизы из избранного
		"""
		response = await self.api.delete("/accounts/users/me/favorites")
		return AccountsUsersMeFavoritesDelete.model_validate(response)

	async def users_me_favorites_ids(
		self,
	) -> AccountsUsersMeFavoritesIds:
		"""
		Список идентификаторов релизов добавленных в избранное
		"""
		response = await self.api.get("/accounts/users/me/favorites/ids")
		return AccountsUsersMeFavoritesIds.model_validate(response)

	async def users_me_favorites_post(
		self,
	) -> AccountsUsersMeFavoritesUpdate:
		"""
		Добавить релизы в избранное
		"""
		response = await self.api.post("/accounts/users/me/favorites")
		return AccountsUsersMeFavoritesUpdate.model_validate(response)

	async def users_me_favorites_references_age_ratings(
		self,
	) -> AccountsUsersMeFavoritesReferencesAgeRatings:
		"""
		Список возрастных рейтингов в избранном пользователя
		"""
		response = await self.api.get("/accounts/users/me/favorites/references/age-ratings")
		return AccountsUsersMeFavoritesReferencesAgeRatings.model_validate(response)

	async def users_me_favorites_references_genres(
		self,
	) -> AccountsUsersMeFavoritesReferencesGenres:
		"""
		Список жанров в избранном пользователя
		"""
		response = await self.api.get("/accounts/users/me/favorites/references/genres")
		return AccountsUsersMeFavoritesReferencesGenres.model_validate(response)

	async def users_me_favorites_references_sorting(
		self,
	) -> AccountsUsersMeFavoritesReferencesSorting:
		"""
		Список опций сортировки в избранном пользователя
		"""
		response = await self.api.get("/accounts/users/me/favorites/references/sorting")
		return AccountsUsersMeFavoritesReferencesSorting.model_validate(response)

	async def users_me_favorites_references_types(
		self,
	) -> AccountsUsersMeFavoritesReferencesTypes:
		"""
		Список типов релизов в избранном пользователя
		"""
		response = await self.api.get("/accounts/users/me/favorites/references/types")
		return AccountsUsersMeFavoritesReferencesTypes.model_validate(response)

	async def users_me_favorites_references_years(
		self,
	) -> AccountsUsersMeFavoritesReferencesYears:
		"""
		Список годов выхода релизов в избранном пользователя
		"""
		response = await self.api.get("/accounts/users/me/favorites/references/years")
		return AccountsUsersMeFavoritesReferencesYears.model_validate(response)

	async def users_me_favorites_releases_get(
		self,
		page: int | None = None,
		limit: int | None = None,
		f_years: str | None = None,
		f_types: list[AnimeReleasesReleaseType] | None = None,
		f_genres: str | None = None,
		f_search: str | None = None,
		f_sorting: AccountsUsersUserFavoriteFilterSorting | None = None,
		f_age_ratings: list[AnimeReleasesReleaseAgeRating] | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AccountsUsersMeFavoritesReleases:
		"""
		Список релизов в избранном пользователя
		:param page: Номер страницы
		:param limit: Ограничение на количество элементов
		:param f_years: Года выхода релиза
		:param f_types: Список типов релизов
		:param f_genres: Список идентификаторов жанров
		:param f_search: Поисковый запрос
		:param f_sorting: Тип сортировки
		:param f_age_ratings: Список возрастных рейтингов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"page": page, "limit": limit, "f[years]": f_years, "f[types]": ([v.value for v in f_types] if f_types is not None else None), "f[genres]": f_genres, "f[search]": f_search, "f[sorting]": (f_sorting.value if f_sorting is not None else None), "f[age_ratings]": ([v.value for v in f_age_ratings] if f_age_ratings is not None else None), "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/accounts/users/me/favorites/releases", params=params)
		return AccountsUsersMeFavoritesReleases.model_validate(response)

	async def users_me_favorites_releases_post(
		self,
		page: int | None = None,
		limit: int | None = None,
		f: dict | None = None,
		include: str | None = None,
		exclude: str | None = None
	) -> AccountsUsersMeFavoritesReleases:
		"""
		Список релизов в избранном пользователя
		:param page: Страница в выдаче
		:param limit: Количество релизов в выдаче
		"""
		data = {"page": page, "limit": limit, "f": f, "include": include, "exclude": exclude}
		response = await self.api.post("/accounts/users/me/favorites/releases", json_data=data)
		return AccountsUsersMeFavoritesReleases.model_validate(response)

	async def users_me_profile(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> UsersV1User:
		"""
		Профиль авторизованного пользователя
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/accounts/users/me/profile", params=params)
		return UsersV1User.model_validate(response)

	async def users_me_views_history(
		self,
		page: int | None = None,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AccountsUsersMeViewsHistory:
		"""
		История просмотренных эпизодов
		:param page: Номер страницы
		:param limit: Ограничение на количество элементов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"page": page, "limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/accounts/users/me/views/history", params=params)
		return AccountsUsersMeViewsHistory.model_validate(response)

	async def users_me_views_timecodes_delete(
		self,
	):
		"""
		Удаление таймкодов просмотра эпизодов
		"""
		return await self.api.delete("/accounts/users/me/views/timecodes")

	async def users_me_views_timecodes_get(
		self,
		since: datetime.datetime | None = None
	):
		"""
		Таймкоды просмотренных эпизодов
		:param since: Возвращает только таймкоды, которые были добавлены после указанного времени (в iso формате)
		"""
		params = {k: v for k, v in {"since": since}.items() if v is not None}
		return await self.api.get("/accounts/users/me/views/timecodes", params=params)

	async def users_me_views_timecodes_post(
		self,
	):
		"""
		Обновление таймкодов прогресса просмотренного эпизода
		"""
		return await self.api.post("/accounts/users/me/views/timecodes")

