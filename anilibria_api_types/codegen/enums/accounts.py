# Auto-generated for enums in accounts category
from enum import StrEnum


class AccountsUsersUserSocialType(StrEnum):
    VK = "vk"
    GOOGLE = "google"
    PATREON = "patreon"
    DISCORD = "discord"


class AccountsUsersUserCollectionType(StrEnum):
    PLANNED = "PLANNED"
    WATCHED = "WATCHED"
    WATCHING = "WATCHING"
    POSTPONED = "POSTPONED"
    ABANDONED = "ABANDONED"


class AccountsUsersUserFavoriteFilterSorting(StrEnum):
    CREATED_AT_DESC = "CREATED_AT_DESC"
    CREATED_AT_ASC = "CREATED_AT_ASC"
    FRESH_AT_DESC = "FRESH_AT_DESC"
    FRESH_AT_ASC = "FRESH_AT_ASC"
    RATING_DESC = "RATING_DESC"
    RATING_ASC = "RATING_ASC"
    YEAR_DESC = "YEAR_DESC"
    YEAR_ASC = "YEAR_ASC"
