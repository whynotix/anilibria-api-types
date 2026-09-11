# Auto-generated for methods in media category
from __future__ import annotations

from anilibria_api_types.codegen.responses.models import (
    AdsVasts,
    MediaPromotions,
    MediaVideos,
)
from anilibria_api_types.methods.base_method import BaseMethod


class MediaMethod(BaseMethod):
    async def manifest_xml(
        self,
    ):
        """
        VAST XML с цепочкой реклам
        """
        return await self.api.get("/media/manifest.xml")

    async def promotions(
        self,
        include: str | list[str] | None = None,
        exclude: str | list[str] | None = None,
    ) -> MediaPromotions:
        """
        Список промо-материалов
        :param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
        :param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
        """
        params = {
            k: v
            for k, v in {"include": include, "exclude": exclude}.items()
            if v is not None
        }
        response = await self.api.get("/media/promotions", params=params)
        return MediaPromotions.model_validate(response)

    async def vasts(
        self,
    ) -> AdsVasts:
        """
        Список возможных VAST реклам
        """
        response = await self.api.get("/media/vasts")
        return AdsVasts.model_validate(response)

    async def videos(
        self,
        limit: int | None = None,
        include: str | list[str] | None = None,
        exclude: str | list[str] | None = None,
    ) -> MediaVideos:
        """
        Список видео-роликов
        :param limit: Количество роликов в выдаче
        :param include: Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
        :param exclude: Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
        """
        params = {
            k: v
            for k, v in {
                "limit": limit,
                "include": include,
                "exclude": exclude,
            }.items()
            if v is not None
        }
        response = await self.api.get("/media/videos", params=params)
        return MediaVideos.model_validate(response)
