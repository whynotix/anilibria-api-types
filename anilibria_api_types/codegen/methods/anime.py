# Auto-generated for methods in anime category
from __future__ import annotations

import uuid
from typing import Any, Union
from anilibria_api_types.codegen.enums.anime import AnimeCatalogFilterProductionStatus, AnimeCatalogFilterPublishStatus, AnimeCatalogFilterSorting, AnimeReleasesReleaseAgeRating, AnimeReleasesReleaseSeason, AnimeReleasesReleaseType
from anilibria_api_types.codegen.responses.models import AnimeCatalogReferencesAgeRatings, AnimeCatalogReferencesGenres, AnimeCatalogReferencesProductionStatuses, AnimeCatalogReferencesPublishStatuses, AnimeCatalogReferencesSeasons, AnimeCatalogReferencesSorting, AnimeCatalogReferencesTypes, AnimeCatalogReferencesYears, AnimeCatalogReleases, AnimeFranchise, AnimeFranchises, AnimeFranchisesByRelease, AnimeFranchisesRandom, AnimeGenres, AnimeGenresItem, AnimeGenresList, AnimeGenresReleases, AnimeReleasesEpisode, AnimeReleasesEpisodeTimecode, AnimeReleasesLatest, AnimeReleasesList, AnimeReleasesRandom, AnimeReleasesRecommended, AnimeReleasesRelease, AnimeReleasesReleaseEpisodesTimecodes, AnimeReleasesReleaseMembers, AnimeScheduleNow, AnimeScheduleWeek, AnimeTorrent, AnimeTorrents, AnimeTorrentsReleaseTorrents

from anilibria_api_types.methods.base_method import BaseMethod

class AnimeMethod(BaseMethod):
	async def catalog_references_age_ratings(
		self,
	) -> AnimeCatalogReferencesAgeRatings:
		"""
		Список возрастных рейтингов в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/age-ratings")
		return AnimeCatalogReferencesAgeRatings.model_validate(response)

	async def catalog_references_genres(
		self,
	) -> AnimeCatalogReferencesGenres:
		"""
		Список жанров в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/genres")
		return AnimeCatalogReferencesGenres.model_validate(response)

	async def catalog_references_production_statuses(
		self,
	) -> AnimeCatalogReferencesProductionStatuses:
		"""
		Список возможных статусов озвучки релиза в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/production-statuses")
		return AnimeCatalogReferencesProductionStatuses.model_validate(response)

	async def catalog_references_publish_statuses(
		self,
	) -> AnimeCatalogReferencesPublishStatuses:
		"""
		Список возможных статусов выхода релиза в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/publish-statuses")
		return AnimeCatalogReferencesPublishStatuses.model_validate(response)

	async def catalog_references_seasons(
		self,
	) -> AnimeCatalogReferencesSeasons:
		"""
		Список сезонов релиза в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/seasons")
		return AnimeCatalogReferencesSeasons.model_validate(response)

	async def catalog_references_sorting(
		self,
	) -> AnimeCatalogReferencesSorting:
		"""
		Список возможных типов сортировок в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/sorting")
		return AnimeCatalogReferencesSorting.model_validate(response)

	async def catalog_references_types(
		self,
	) -> AnimeCatalogReferencesTypes:
		"""
		Список типов релизов в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/types")
		return AnimeCatalogReferencesTypes.model_validate(response)

	async def catalog_references_years(
		self,
	) -> AnimeCatalogReferencesYears:
		"""
		Список годов в каталоге
		"""
		response = await self.api.get("/anime/catalog/references/years")
		return AnimeCatalogReferencesYears.model_validate(response)

	async def catalog_releases_get(
		self,
		page: int | None = None,
		limit: int | None = None,
		f_genres: str | None = None,
		f_types: list[AnimeReleasesReleaseType] | None = None,
		f_seasons: list[AnimeReleasesReleaseSeason] | None = None,
		f_years_from_year: str | None = None,
		f_years_to_year: str | None = None,
		f_search: str | None = None,
		f_sorting: AnimeCatalogFilterSorting | None = None,
		f_age_ratings: list[AnimeReleasesReleaseAgeRating] | None = None,
		f_publish_statuses: list[AnimeCatalogFilterPublishStatus] | None = None,
		f_production_statuses: list[AnimeCatalogFilterProductionStatus] | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeCatalogReleases:
		"""
		Список релизов в каталоге
		:param page: Номер страницы
		:param limit: Ограничение на количество элементов
		:param f_genres: Список идентификаторов жанров
		:param f_types: Список типов релизов
		:param f_seasons: Список сезонов релизов
		:param f_years_from_year: Минимальный год выхода релиза
		:param f_years_to_year: Максимальный год выхода релиза
		:param f_search: Поиск запрос
		:param f_sorting: Тип сортировки
		:param f_age_ratings: Список возрастных рейтингов
		:param f_publish_statuses: Список статусов релизов
		:param f_production_statuses: Список статусов релизов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"page": page, "limit": limit, "f[genres]": f_genres, "f[types]": ([v.value for v in f_types] if f_types is not None else None), "f[seasons]": ([v.value for v in f_seasons] if f_seasons is not None else None), "f[years][from_year]": f_years_from_year, "f[years][to_year]": f_years_to_year, "f[search]": f_search, "f[sorting]": (f_sorting.value if f_sorting is not None else None), "f[age_ratings]": ([v.value for v in f_age_ratings] if f_age_ratings is not None else None), "f[publish_statuses]": ([v.value for v in f_publish_statuses] if f_publish_statuses is not None else None), "f[production_statuses]": ([v.value for v in f_production_statuses] if f_production_statuses is not None else None), "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/catalog/releases", params=params)
		return AnimeCatalogReleases.model_validate(response)

	async def catalog_releases_post(
		self,
		page: int | None = None,
		limit: int | None = None,
		f: dict | None = None,
		include: str | None = None,
		exclude: str | None = None
	) -> AnimeCatalogReleases:
		"""
		Список релизов в каталоге
		"""
		data = {"page": page, "limit": limit, "f": f, "include": include, "exclude": exclude}
		response = await self.api.post("/anime/catalog/releases", json_data=data)
		return AnimeCatalogReleases.model_validate(response)

	async def franchises(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeFranchises:
		"""
		Получить список франшиз
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/franchises", params=params)
		return AnimeFranchises.model_validate(response)

	async def franchises_franchiseid(
		self,
		franchiseid: str,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeFranchise:
		"""
		Получить франшизу
		:param franchiseid: ID франшизы
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/franchises/{franchiseid}", params=params)
		return AnimeFranchise.model_validate(response)

	async def franchises_random(
		self,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeFranchisesRandom:
		"""
		Получить список случайных франшиз
		:param limit: Количество случайных франшиз в выдаче
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/franchises/random", params=params)
		return AnimeFranchisesRandom.model_validate(response)

	async def franchises_release_releaseid(
		self,
		releaseid: str,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeFranchisesByRelease:
		"""
		Получить список франшиз для релиза
		:param releaseid: ID релиза
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/franchises/release/{releaseid}", params=params)
		return AnimeFranchisesByRelease.model_validate(response)

	async def genres(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeGenres:
		"""
		Список всех жанров
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/genres", params=params)
		return AnimeGenres.model_validate(response)

	async def genres_genreid(
		self,
		genreid: int,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeGenresItem:
		"""
		Данные по жанру
		:param genreid: ID Жанра
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/genres/{genreid}", params=params)
		return AnimeGenresItem.model_validate(response)

	async def genres_genreid_releases(
		self,
		genreid: int,
		page: int | None = None,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeGenresReleases:
		"""
		Список релизов жанра
		:param genreid: ID Жанра
		:param page: Номер страницы
		:param limit: Ограничение на количество элементов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"page": page, "limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/genres/{genreid}/releases", params=params)
		return AnimeGenresReleases.model_validate(response)

	async def genres_random(
		self,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeGenresList:
		"""
		Список случайных жанров
		:param limit: Количество жанров в выдаче
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/genres/random", params=params)
		return AnimeGenresList.model_validate(response)

	async def releases_episodes_releaseepisodeid(
		self,
		releaseepisodeid: uuid.UUID,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesEpisode:
		"""
		Данные по эпизоду
		:param releaseepisodeid: Идентификатор эпизода
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/releases/episodes/{releaseepisodeid}", params=params)
		return AnimeReleasesEpisode.model_validate(response)

	async def releases_episodes_releaseepisodeid_timecode(
		self,
		releaseepisodeid: uuid.UUID,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesEpisodeTimecode:
		"""
		Данные по просмотру эпизода
		:param releaseepisodeid: Идентификатор эпизода
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/releases/episodes/{releaseepisodeid}/timecode", params=params)
		return AnimeReleasesEpisodeTimecode.model_validate(response)

	async def releases_idoralias(
		self,
		idoralias: Any,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesRelease:
		"""
		Данные по релизу
		:param idoralias: id или alias релиза
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/releases/{idoralias}", params=params)
		return AnimeReleasesRelease.model_validate(response)

	async def releases_idoralias_episodes_timecodes(
		self,
		idoralias: str,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesReleaseEpisodesTimecodes:
		"""
		Данные по таймкодам просмотра эпизодов релиза
		:param idoralias: id или alias релиза
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/releases/{idoralias}/episodes/timecodes", params=params)
		return AnimeReleasesReleaseEpisodesTimecodes.model_validate(response)

	async def releases_idoralias_members(
		self,
		idoralias: str,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesReleaseMembers:
		"""
		Список участников, которые работали над релизом
		:param idoralias: id или alias релиза
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/releases/{idoralias}/members", params=params)
		return AnimeReleasesReleaseMembers.model_validate(response)

	async def releases_latest(
		self,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesLatest:
		"""
		Последние релизы
		:param limit: Количество последних релизов в выдаче
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/releases/latest", params=params)
		return AnimeReleasesLatest.model_validate(response)

	async def releases_list(
		self,
		ids: list[int] | None = None,
		aliases: list[str] | None = None,
		page: int | None = None,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesList:
		"""
		Данные по списку релизов
		:param ids: Список ID релизов
		:param aliases: Список alias релизов
		:param page: Номер страницы
		:param limit: Ограничение на количество элементов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"ids": ids, "aliases": aliases, "page": page, "limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/releases/list", params=params)
		return AnimeReleasesList.model_validate(response)

	async def releases_random(
		self,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesRandom:
		"""
		Данные по случайным релизам
		:param limit: Количество случайных релизов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/releases/random", params=params)
		return AnimeReleasesRandom.model_validate(response)

	async def releases_recommended(
		self,
		limit: int | None = None,
		release_id: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeReleasesRecommended:
		"""
		Данные по рекомендованным релизам
		:param limit: Количество рекомендованных релизов
		:param release_id: Идентификатор релиза, для которого рекомендуем
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"limit": limit, "release_id": release_id, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/releases/recommended", params=params)
		return AnimeReleasesRecommended.model_validate(response)

	async def schedule_now(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeScheduleNow:
		"""
		Данные по расписанию релизов на текущую дату
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/schedule/now", params=params)
		return AnimeScheduleNow.model_validate(response)

	async def schedule_week(
		self,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeScheduleWeek:
		"""
		Данные по расписанию релизов на текущую неделю
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/schedule/week", params=params)
		return AnimeScheduleWeek.model_validate(response)

	async def torrents(
		self,
		page: int | None = None,
		limit: int | None = None,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeTorrents:
		"""
		Данные по торрентам
		:param page: Номер страницы
		:param limit: Ограничение на количество элементов
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"page": page, "limit": limit, "include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get("/anime/torrents", params=params)
		return AnimeTorrents.model_validate(response)

	async def torrents_hashorid(
		self,
		hashorid: str,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeTorrent:
		"""
		Данные по торренту
		:param hashorid: Hash или ID торрента
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/torrents/{hashorid}", params=params)
		return AnimeTorrent.model_validate(response)

	async def torrents_hashorid_file(
		self,
		hashorid: str,
		pk: str | None = None
	):
		"""
		Торрент-файл по его hash или id
		:param hashorid: Hash или ID торрента
		:param pk: passkey пользователя. Оставьте пустым для собственного pk (если аутентифицирован)
		"""
		params = {k: v for k, v in {"pk": pk}.items() if v is not None}
		return await self.api.get(f"/anime/torrents/{hashorid}/file", params=params)

	async def torrents_release_releaseid(
		self,
		releaseid: int,
		include: Union[str, list[str]] | None = None,
		exclude: Union[str, list[str]] | None = None
	) -> AnimeTorrentsReleaseTorrents:
		"""
		Данные по торрентам для релиза
		:param releaseid: ID релиза
		:param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
		:param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
		"""
		params = {k: v for k, v in {"include": include, "exclude": exclude}.items() if v is not None}
		response = await self.api.get(f"/anime/torrents/release/{releaseid}", params=params)
		return AnimeTorrentsReleaseTorrents.model_validate(response)

	async def torrents_rss(
		self,
		limit: int | None = None,
		pk: str | None = None
	):
		"""
		RSS лента последних торрентов
		:param limit: Количество торрентов в выдаче. По умолчанию 10
		:param pk: Пользовательский passkey. Персонализирует ссылки на торренты для учета статистики
		"""
		params = {k: v for k, v in {"limit": limit, "pk": pk}.items() if v is not None}
		return await self.api.get("/anime/torrents/rss", params=params)

	async def torrents_rss_release_releaseid(
		self,
		releaseid: int,
		pk: str | None = None
	):
		"""
		RSS лента торрентов релиза
		:param releaseid: ID релиза
		:param pk: Пользовательский passkey. Персонализирует ссылки на торренты для учета статистики
		"""
		params = {k: v for k, v in {"pk": pk}.items() if v is not None}
		return await self.api.get(f"/anime/torrents/rss/release/{releaseid}", params=params)

