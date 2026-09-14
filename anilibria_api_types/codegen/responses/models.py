# Auto-generated responses/models
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, RootModel


if TYPE_CHECKING:
    import datetime
    import uuid

    from anilibria_api_types.codegen.enums.accounts import (
        AccountsUsersUserCollectionType,
        AccountsUsersUserFavoriteFilterSorting,
    )
    from anilibria_api_types.codegen.enums.ads import AdsBannerPlacement
    from anilibria_api_types.codegen.enums.anime import (
        AnimeCatalogFilterProductionStatus,
        AnimeCatalogFilterPublishStatus,
        AnimeCatalogFilterSorting,
        AnimeReleasesReleaseAgeRating,
        AnimeReleasesReleaseMemberRole,
        AnimeReleasesReleasePublishDay,
        AnimeReleasesReleaseSeason,
        AnimeReleasesReleaseType,
        AnimeTorrentsTorrentCodec,
        AnimeTorrentsTorrentColor,
        AnimeTorrentsTorrentMemberRole,
        AnimeTorrentsTorrentQuality,
        AnimeTorrentsTorrentType,
    )
    from anilibria_api_types.codegen.enums.media import (
        MediaVideosVideoOriginType,
    )


class HttpResponses422Content(BaseModel):
    errors: dict[str, list[str]] | None = None


class ModelsComponentsImage(BaseModel):
    preview: str | None = None
    thumbnail: str | None = None


class ModelsComponentsImageWithOptimized(ModelsComponentsImage):
    optimized: ModelsComponentsImage | None = None


class UtilsPaginationSchemesMeta(BaseModel):
    pagination: UtilsPaginationSchemesMetaPagination | None = None


class UtilsPaginationSchemesMetaPagination(BaseModel):
    total: int | None = None
    count: int | None = None
    per_page: int | None = None
    current_page: int | None = None
    total_pages: int | None = None
    links: UtilsPaginationSchemesMetaPaginationLinks | None = None


class UtilsPaginationSchemesMetaPaginationLinks(BaseModel):
    previous: str | None = None
    next: str | None = None


class AccountsOtpLogin(BaseModel):
    token: str | None = None


class AccountsOtpGet(BaseModel):
    otp: AccountsOtpV1Otp | None = None
    remaining_time: int | None = None


class AccountsOtpV1Otp(BaseModel):
    code: str | None = None
    user_id: int | None = None
    device_id: str | None = None
    expired_at: datetime.datetime | None = None


class AccountsUsersMeCollectionsReferencesAgeRatings(RootModel):
    root: list[AccountsUsersMeCollectionsReferencesAgeRatingsItem]


class AccountsUsersMeCollectionsReferencesAgeRatingsItem(BaseModel):
    value: AnimeReleasesReleaseAgeRating | None = None
    label: str | None = None
    description: str | None = None


class AccountsUsersMeCollectionsReferencesGenres(RootModel):
    root: list[AccountsUsersMeCollectionsReferencesGenresItem]


class AccountsUsersMeCollectionsReferencesGenresItem(BaseModel):
    id: int | None = None
    name: str | None = None


class AccountsUsersMeCollectionsReferencesTypes(RootModel):
    root: list[AccountsUsersMeCollectionsReferencesTypesItem]


class AccountsUsersMeCollectionsReferencesTypesItem(BaseModel):
    value: AnimeReleasesReleaseType | None = None
    description: str | None = None


class AccountsUsersMeCollectionsReferencesYears(RootModel):
    root: list[int]


class AccountsUsersCollectionsReleases(BaseModel):
    data: list[AccountsUsersCollectionsReleasesItem] | None = None
    meta: UtilsPaginationSchemesMeta | None = None


class AnimeReleasesV1Release(BaseModel):
    id: float | None = None
    type: AnimeReleasesV1ReleaseType | None = None
    year: float | None = None
    name: AnimeReleasesV1ReleaseName | None = None
    alias: str | None = None
    season: AnimeReleasesV1ReleaseSeason | None = None
    shikimori: AnimeReleasesV1ReleaseShikimori | None = None
    mal: AnimeReleasesV1ReleaseMal | None = None
    rating: AnimeReleasesV1ReleaseRating | None = None
    poster: ModelsComponentsImageWithOptimized | None = None
    fresh_at: datetime.datetime | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
    is_ongoing: bool | None = None
    age_rating: AnimeReleasesV1ReleaseAgeRating | None = None
    publish_day: AnimeReleasesV1ReleasePublishDay | None = None
    description: str | None = None
    notification: str | None = None
    episodes_total: float | None = None
    external_player: str | None = None
    is_in_production: bool | None = None
    is_blocked_by_geo: bool | None = None
    is_blocked_by_copyrights: bool | None = None
    added_in_users_favorites: float | None = None
    average_duration_of_episode: float | None = None
    added_in_planned_collection: float | None = None
    added_in_watched_collection: float | None = None
    added_in_watching_collection: float | None = None
    added_in_postponed_collection: float | None = None
    added_in_abandoned_collection: float | None = None


class AccountsUsersCollectionsReleasesItem(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None
    episodes: list[AnimeReleasesV1ReleaseEpisode] | None = None


class AccountsUsersMeFavoritesReferencesAgeRatings(RootModel):
    root: list[AccountsUsersMeFavoritesReferencesAgeRatingsItem]


class AccountsUsersMeFavoritesReferencesAgeRatingsItem(BaseModel):
    value: AnimeReleasesReleaseAgeRating | None = None
    label: str | None = None
    description: str | None = None


class AccountsUsersMeFavoritesReferencesGenres(RootModel):
    root: list[AccountsUsersMeFavoritesReferencesGenresItem]


class AccountsUsersMeFavoritesReferencesGenresItem(BaseModel):
    id: int | None = None
    name: str | None = None


class AccountsUsersMeFavoritesReferencesSorting(RootModel):
    root: list[AccountsUsersMeFavoritesReferencesSortingItem]


class AccountsUsersMeFavoritesReferencesSortingItem(BaseModel):
    value: AccountsUsersUserFavoriteFilterSorting | None = None
    label: str | None = None
    description: str | None = None


class AccountsUsersMeFavoritesReferencesTypes(RootModel):
    root: list[AccountsUsersMeFavoritesReferencesTypesItem]


class AccountsUsersMeFavoritesReferencesTypesItem(BaseModel):
    value: AnimeReleasesReleaseType | None = None
    description: str | None = None


class AccountsUsersMeFavoritesReferencesYears(RootModel):
    root: list[int]


class AccountsUsersMeFavoritesReleases(BaseModel):
    data: list[AccountsUsersMeFavoritesReleasesItem] | None = None
    meta: UtilsPaginationSchemesMeta | None = None


class AccountsUsersMeFavoritesReleasesItem(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None
    episodes: list[AnimeReleasesV1ReleaseEpisode] | None = None


class AccountsUsersMeViewsHistory(BaseModel):
    data: list[AccountsUsersMeViewsHistoryItem] | None = None
    meta: UtilsPaginationSchemesMeta | None = None


class AccountsUsersV1UserView(BaseModel):
    id: int | None = None
    time: int | None = None
    user_id: int | None = None
    is_watched: bool | None = None
    updated_at: datetime.datetime | None = None
    release_episode_id: str | None = None


class AccountsUsersMeViewsHistoryItem(AccountsUsersV1UserView):
    release_episode: AccountsUsersMeViewsHistoryItemReleaseEpisode | None = (
        None
    )


class AnimeReleasesV1ReleaseEpisode(BaseModel):
    id: str | None = None
    name: str | None = None
    ordinal: float | None = None
    ending: AnimeReleasesV1ReleaseEpisodeSkip | None = None
    opening: AnimeReleasesV1ReleaseEpisodeSkip | None = None
    preview: ModelsComponentsImageWithOptimized | None = None
    hls_480: str | None = None
    hls_720: str | None = None
    hls_1080: str | None = None
    duration: float | None = None
    rutube_id: str | None = None
    youtube_id: str | None = None
    updated_at: datetime.datetime | None = None
    sort_order: float | None = None
    release_id: float | None = None
    name_english: str | None = None


class AccountsUsersMeViewsHistoryItemReleaseEpisode(
    AnimeReleasesV1ReleaseEpisode
):
    release: AnimeReleasesV1Release | None = None


class AccountsUsersAuthLogin(BaseModel):
    token: str | None = None


class AccountsUsersAuthSocialAuthenticate(BaseModel):
    token: str | None = None


class AccountsUsersAuthSocialLogin(BaseModel):
    url: str | None = None
    state: str | None = None


class AccountsUsersAuthLogout(BaseModel):
    token: None = None


class AccountsUsersMeCollectionsDelete(RootModel):
    root: list[AccountsUsersMeCollectionsIdsItem]


class AccountsUsersMeCollectionsIds(RootModel):
    root: list[AccountsUsersMeCollectionsIdsItem]


class AccountsUsersMeCollectionsIdsItem(RootModel):
    root: float | AccountsUsersUserCollectionType


class AccountsUsersMeCollectionsUpdate(RootModel):
    root: list[AccountsUsersMeCollectionsIdsItem]


class AccountsUsersMeFavoritesDelete(RootModel):
    root: list[AccountsUsersMeFavoritesIdsItem]


class AccountsUsersMeFavoritesIdsItem(RootModel):
    root: int


class AccountsUsersMeFavoritesIds(RootModel):
    root: list[AccountsUsersMeFavoritesIdsItem]


class AccountsUsersMeFavoritesUpdate(RootModel):
    root: list[AccountsUsersMeFavoritesIdsItem]


class AccountsUsersMeViewsTimecodesItem(RootModel):
    root: uuid.UUID | float | bool


class AccountsUsersMeViewsTimecodes(RootModel):
    root: list[AccountsUsersMeViewsTimecodesItem]


class UsersV1UserSession(BaseModel):
    id: str | None = None
    user_id: int | None = None
    device: UsersV1UserSessionDevice | None = None
    browser: UsersV1UserSessionBrowser | None = None
    location: UsersV1UserSessionLocation | None = None
    is_mobile: bool | None = None
    is_desktop: bool | None = None
    ip_address: str | None = None
    user_agent: str | None = None
    is_current: bool | None = None
    last_active: datetime.datetime | None = None


class UsersV1UserSessionDevice(BaseModel):
    name: str | None = None
    version: str | None = None
    platform: str | None = None


class UsersV1UserSessionBrowser(BaseModel):
    name: str | None = None
    version: str | None = None


class UsersV1UserSessionLocation(BaseModel):
    country: str | None = None
    iso_code: str | None = None


class UsersV1User(BaseModel):
    id: int | None = None
    login: str | None = None
    email: str | None = None
    nickname: str | None = None
    avatar: ModelsComponentsImageWithOptimized | None = None
    torrents: UsersV1UserTorrents | None = None
    is_banned: bool | None = None
    created_at: datetime.datetime | None = None
    is_with_ads: bool | None = None


class UsersV1UserTorrents(BaseModel):
    passkey: str | None = None
    uploaded: int | None = None
    downloaded: int | None = None


class AdsBannersV1Banner(BaseModel):
    id: int | None = None
    title: str | None = None
    image: ModelsComponentsImageWithOptimized | None = None
    ad_erid: str | None = None
    image_url: str | None = None
    button_url: str | None = None
    placement: AdsBannerPlacement | None = None
    has_overlay: bool | None = None
    button_title: str | None = None
    description: str | None = None
    ad_company_itn: str | None = None
    ad_company_name: str | None = None


class AdsVasts(RootModel):
    root: list[AdsVastsV1Vast]


class AdsVastsV1Vast(BaseModel):
    id: str | None = None
    url: str | None = None
    ad_erid: str | None = None
    ad_company_itn: str | None = None
    ad_company_name: str | None = None


class AnimeCatalogReleases(BaseModel):
    data: list[AnimeCatalogReleasesItem] | None = None
    meta: UtilsPaginationSchemesMeta | None = None


class AnimeCatalogReleasesItem(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None


class AnimeCatalogReferencesAgeRatings(RootModel):
    root: list[AnimeCatalogReferencesAgeRatingsItem]


class AnimeCatalogReferencesAgeRatingsItem(BaseModel):
    value: AnimeReleasesReleaseAgeRating | None = None
    label: str | None = None
    description: str | None = None


class AnimeCatalogReferencesGenres(RootModel):
    root: list[AnimeCatalogReferencesGenresItem]


class AnimeCatalogReferencesGenresItem(BaseModel):
    id: int | None = None
    name: str | None = None


class AnimeCatalogReferencesProductionStatuses(RootModel):
    root: list[AnimeCatalogReferencesProductionStatusesItem]


class AnimeCatalogReferencesProductionStatusesItem(BaseModel):
    value: AnimeCatalogFilterProductionStatus | None = None
    description: str | None = None


class AnimeCatalogReferencesPublishStatuses(RootModel):
    root: list[AnimeCatalogReferencesPublishStatusesItem]


class AnimeCatalogReferencesPublishStatusesItem(BaseModel):
    value: AnimeCatalogFilterPublishStatus | None = None
    description: str | None = None


class AnimeCatalogReferencesSeasons(RootModel):
    root: list[AnimeCatalogReferencesSeasonsItem]


class AnimeCatalogReferencesSeasonsItem(BaseModel):
    value: AnimeReleasesReleaseSeason | None = None
    description: str | None = None


class AnimeCatalogReferencesSorting(RootModel):
    root: list[AnimeCatalogReferencesSortingItem]


class AnimeCatalogReferencesSortingItem(BaseModel):
    value: AnimeCatalogFilterSorting | None = None
    label: str | None = None
    description: str | None = None


class AnimeCatalogReferencesTypes(RootModel):
    root: list[AnimeCatalogReferencesTypesItem]


class AnimeCatalogReferencesTypesItem(BaseModel):
    value: AnimeReleasesReleaseType | None = None
    description: str | None = None


class AnimeCatalogReferencesYears(RootModel):
    root: list[int]


class AnimeFranchises(RootModel):
    root: list[AnimeFranchisesV1Franchise]


class AnimeFranchisesV1Franchise(BaseModel):
    id: str | None = None
    name: str | None = None
    name_english: str | None = None
    image: ModelsComponentsImageWithOptimized | None = None
    rating: float | None = None
    last_year: int | None = None
    first_year: int | None = None
    total_releases: int | None = None
    total_episodes: int | None = None
    total_duration: str | None = None
    total_duration_in_seconds: int | None = None


class AnimeFranchise(AnimeFranchisesV1Franchise):
    franchise_releases: list[AnimeFranchiseItem] | None = None


class AnimeFranchisesV1FranchiseRelease(BaseModel):
    id: str | None = None
    sort_order: int | None = None
    release_id: int | None = None
    franchise_id: str | None = None


class AnimeFranchiseItem(AnimeFranchisesV1FranchiseRelease):
    release: AnimeReleasesV1Release | None = None


class AnimeFranchisesRandom(RootModel):
    root: list[AnimeFranchisesV1Franchise]


class AnimeFranchisesByRelease(RootModel):
    root: list[AnimeFranchisesByReleaseItem]


class AnimeFranchisesByReleaseItem(AnimeFranchisesV1Franchise):
    franchise_releases: list[AnimeFranchisesByReleaseItemItem] | None = None


class AnimeFranchisesByReleaseItemItem(AnimeFranchisesV1FranchiseRelease):
    release: AnimeReleasesV1Release | None = None


class AnimeGenres(RootModel):
    root: list[AnimeGenresV1Genre]


class AnimeGenresV1Genre(BaseModel):
    id: int | None = None
    name: str | None = None
    image: ModelsComponentsImageWithOptimized | None = None
    total_releases: int | None = None


class AnimeGenresItem(AnimeGenresV1Genre):
    pass


class AnimeGenresList(RootModel):
    root: list[AnimeGenresV1Genre]


class AnimeGenresReleases(BaseModel):
    data: list[AnimeReleasesV1Release] | None = None
    meta: UtilsPaginationSchemesMeta | None = None


class AnimeReleasesRandom(RootModel):
    root: list[AnimeReleasesRandomItem]


class AnimeReleasesRandomItem(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None
    background_covers: list[ModelsComponentsImage] | None = None


class AnimeReleasesRecommended(RootModel):
    root: list[AnimeReleasesRecommendedItem]


class AnimeReleasesRecommendedItem(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None


class AnimeReleasesLatest(RootModel):
    root: list[AnimeReleasesLatestItem]


class AnimeReleasesLatestItem(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None
    latest_episode: AnimeReleasesV1ReleaseEpisode | None = None


class AnimeReleasesList(BaseModel):
    data: list[AnimeReleasesListItem] | None = None
    meta: UtilsPaginationSchemesMeta | None = None


class AnimeReleasesListItem(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None
    members: list[AnimeReleasesV1ReleaseMember] | None = None
    episodes: list[AnimeReleasesV1ReleaseEpisode] | None = None
    torrents: list[AnimeTorrentsV1Torrent] | None = None
    sponsors: list[AnimeSponsorsV1Sponsor] | None = None


class AnimeReleasesRelease(AnimeReleasesV1Release):
    genres: list[AnimeGenresV1Genre] | None = None
    members: list[AnimeReleasesV1ReleaseMember] | None = None
    episodes: list[AnimeReleasesV1ReleaseEpisode] | None = None
    torrents: list[AnimeTorrentsV1Torrent] | None = None
    sponsors: list[AnimeSponsorsV1Sponsor] | None = None
    background_covers: list[ModelsComponentsImage] | None = None


class AnimeReleasesReleaseMembers(RootModel):
    root: list[AnimeReleasesV1ReleaseMember]


class AnimeReleasesReleaseEpisodesTimecodes(RootModel):
    root: list[AccountsUsersV1UserView]


class AnimeReleasesEpisode(AnimeReleasesV1ReleaseEpisode):
    release: AnimeReleasesEpisodeRelease | None = None


class AnimeReleasesEpisodeRelease(AnimeReleasesV1Release):
    episodes: list[AnimeReleasesV1ReleaseEpisode] | None = None


class AnimeReleasesEpisodeTimecode(AccountsUsersV1UserView):
    pass


class AnimeReleasesV1ReleaseMemberRole(BaseModel):
    value: AnimeReleasesReleaseMemberRole | None = None
    description: str | None = None


class AnimeReleasesV1ReleaseMember(BaseModel):
    id: str | None = None
    role: AnimeReleasesV1ReleaseMemberRole | None = None
    user: AnimeReleasesV1ReleaseMemberUser | None = None
    nickname: str | None = None


class AnimeReleasesV1ReleaseMemberUser(BaseModel):
    id: float | None = None
    avatar: ModelsComponentsImageWithOptimized | None = None


class AnimeReleasesV1ReleaseType(BaseModel):
    value: AnimeReleasesReleaseType | None = None
    description: str | None = None


class AnimeReleasesV1ReleaseName(BaseModel):
    main: str | None = None
    english: str | None = None
    alternative: str | None = None


class AnimeReleasesV1ReleaseSeason(BaseModel):
    value: AnimeReleasesReleaseSeason | None = None
    description: str | None = None


class AnimeReleasesV1ReleaseAgeRating(BaseModel):
    value: AnimeReleasesReleaseAgeRating | None = None
    label: str | None = None
    is_adult: bool | None = None
    description: str | None = None


class AnimeReleasesV1ReleasePublishDay(BaseModel):
    value: AnimeReleasesReleasePublishDay | None = None
    description: str | None = None


class AnimeReleasesV1ReleaseShikimori(BaseModel):
    id: float | None = None
    url: str | None = None
    votes: float | None = None
    rating: float | None = None


class AnimeReleasesV1ReleaseMal(BaseModel):
    id: float | None = None
    url: str | None = None
    votes: float | None = None
    rating: float | None = None


class AnimeReleasesV1ReleaseRating(BaseModel):
    average: float | None = None
    votes: float | None = None
    distribution: dict | None = None


class AnimeReleasesV1ReleaseEpisodeSkip(BaseModel):
    start: float | None = None
    stop: float | None = None


class AnimeReleasesV1ReleaseRatingOwn(BaseModel):
    release_id: float | None = None
    score: float | None = None


class AnimeScheduleNow(BaseModel):
    today: list[AnimeScheduleV1ReleaseInSchedule] | None = None
    tomorrow: list[AnimeScheduleV1ReleaseInSchedule] | None = None
    yesterday: list[AnimeScheduleV1ReleaseInSchedule] | None = None


class AnimeScheduleWeek(BaseModel):
    data: list[AnimeScheduleV1ReleaseInSchedule] | None = None


class AnimeScheduleV1ReleaseInSchedule(BaseModel):
    release: AnimeReleasesV1Release | None = None
    full_season_is_released: bool | None = None
    published_release_episode: AnimeReleasesV1ReleaseEpisode | None = None
    next_release_episode_number: int | None = None


class AnimeSponsorsV1Sponsor(BaseModel):
    id: str | None = None
    title: str | None = None
    description: str | None = None
    url_title: str | None = None
    url: str | None = None


class AnimeTorrents(BaseModel):
    data: list[AnimeTorrentsItem] | None = None
    meta: UtilsPaginationSchemesMeta | None = None


class AnimeTorrentsV1Torrent(BaseModel):
    id: int | None = None
    hash: str | None = None
    size: int | None = None
    type: AnimeTorrentsV1TorrentType | None = None
    color: AnimeTorrentsV1TorrentColor | None = None
    codec: AnimeTorrentsV1TorrentCodec | None = None
    label: str | None = None
    quality: AnimeTorrentsV1TorrentQuality | None = None
    magnet: str | None = None
    filename: str | None = None
    seeders: int | None = None
    bitrate: int | None = None
    leechers: int | None = None
    sort_order: int | None = None
    updated_at: datetime.datetime | None = None
    is_hardsub: bool | None = None
    description: str | None = None
    created_at: datetime.datetime | None = None
    completed_times: int | None = None


class AnimeTorrentsItem(AnimeTorrentsV1Torrent):
    torrent_members: list[AnimeTorrentsItemItem] | None = None
    release: AnimeReleasesV1Release | None = None


class AnimeTorrentsV1TorrentMember(BaseModel):
    id: str | None = None
    role: AnimeTorrentsV1TorrentMemberRole | None = None
    nickname: str | None = None
    external_url: str | None = None


class AnimeTorrentsItemItem(AnimeTorrentsV1TorrentMember):
    user: AnimeTorrentsV1TorrentMemberUser | None = None


class AnimeTorrent(AnimeTorrentsV1Torrent):
    torrent_members: list[AnimeTorrentItem] | None = None
    release: AnimeReleasesV1Release | None = None


class AnimeTorrentItem(AnimeTorrentsV1TorrentMember):
    user: AnimeTorrentsV1TorrentMemberUser | None = None


class AnimeTorrentsReleaseTorrents(RootModel):
    root: list[AnimeTorrentsReleaseTorrentsItem]


class AnimeTorrentsReleaseTorrentsItem(AnimeTorrentsV1Torrent):
    torrent_members: list[AnimeTorrentsReleaseTorrentsItemItem] | None = None
    release: AnimeReleasesV1Release | None = None


class AnimeTorrentsReleaseTorrentsItemItem(AnimeTorrentsV1TorrentMember):
    user: AnimeTorrentsV1TorrentMemberUser | None = None


class AnimeTorrentsV1TorrentMemberRole(BaseModel):
    value: AnimeTorrentsTorrentMemberRole | None = None
    description: str | None = None


class AnimeTorrentsV1TorrentMemberUser(BaseModel):
    id: float | None = None
    avatar: ModelsComponentsImageWithOptimized | None = None


class AnimeTorrentsV1TorrentType(BaseModel):
    value: AnimeTorrentsTorrentType | None = None
    description: str | None = None


class AnimeTorrentsV1TorrentQuality(BaseModel):
    value: AnimeTorrentsTorrentQuality | None = None
    description: str | None = None


class AnimeTorrentsV1TorrentCodec(BaseModel):
    value: AnimeTorrentsTorrentCodec | None = None
    label: str | None = None
    description: str | None = None
    label_color: str | None = None
    label_is_visible: bool | None = None


class AnimeTorrentsV1TorrentColor(BaseModel):
    value: AnimeTorrentsTorrentColor | None = None
    description: str | None = None


class AppSearchReleases(RootModel):
    root: list[AnimeReleasesV1Release]


class AppStatus(BaseModel):
    request: AppStatusRequest | None = None
    is_alive: bool | None = None
    available_api_endpoints: list[str] | None = None


class AppStatusRequest(BaseModel):
    ip: str | None = None
    country: str | None = None
    iso_code: str | None = None
    timezone: str | None = None


class MediaPromotions(BaseModel):
    data: list[MediaPromotionsV1Promotion] | None = None


class MediaPromotionsV1Promotion(BaseModel):
    id: str | None = None
    url: str | None = None
    url_label: str | None = None
    image: ModelsComponentsImageWithOptimized | None = None
    title: str | None = None
    description: str | None = None
    is_ad: bool | None = None
    ad_erid: str | None = None
    ad_origin: str | None = None
    release: AnimeReleasesV1Release | None = None
    has_overlay: bool | None = None


class MediaVideos(BaseModel):
    data: list[MediaVideosItem] | None = None


class MediaVideosV1VideoContent(BaseModel):
    id: int | None = None
    url: str | None = None
    title: str | None = None
    views: int | None = None
    image: ModelsComponentsImageWithOptimized | None = None
    comments: int | None = None
    video_id: str | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
    is_announce: bool | None = None


class MediaVideosItem(MediaVideosV1VideoContent):
    origin: MediaVideosV1VideoOrigin | None = None


class MediaVideosV1VideoOriginType(BaseModel):
    value: MediaVideosVideoOriginType | None = None
    description: str | None = None


class MediaVideosV1VideoOrigin(BaseModel):
    id: str | None = None
    url: str | None = None
    type: MediaVideosV1VideoOriginType | None = None
    title: str | None = None
    description: str | None = None
    is_announce: bool | None = None


class Teams(RootModel):
    root: list[TeamsV1Team]


class TeamsRoles(RootModel):
    root: list[TeamsV1TeamRole]


class TeamsUsers(RootModel):
    root: list[TeamsUsersItem]


class TeamsV1TeamUser(BaseModel):
    id: str | None = None
    nickname: str | None = None
    is_intern: bool | None = None
    sort_order: int | None = None
    is_vacation: bool | None = None


class TeamsUsersItem(TeamsV1TeamUser):
    team: TeamsV1Team | None = None
    user: TeamsV1TeamUserAccount | None = None
    roles: list[TeamsV1TeamRole] | None = None


class TeamsV1TeamRole(BaseModel):
    id: str | None = None
    title: str | None = None
    color: str | None = None
    sort_order: int | None = None


class TeamsV1TeamUserAccount(BaseModel):
    id: int | None = None
    nickname: str | None = None
    avatar: ModelsComponentsImageWithOptimized | None = None


class TeamsV1Team(BaseModel):
    id: str | None = None
    title: str | None = None
    sort_order: int | None = None
    description: str | None = None
