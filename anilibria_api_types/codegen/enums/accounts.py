# Auto-generated for enums in accounts category
from enum import Enum


class AccountsUsersUserSocialType(str, Enum):
	VK = 'vk'
	GOOGLE = 'google'
	PATREON = 'patreon'
	DISCORD = 'discord'


class AccountsUsersUserCollectionType(str, Enum):
	PLANNED = 'PLANNED'
	WATCHED = 'WATCHED'
	WATCHING = 'WATCHING'
	POSTPONED = 'POSTPONED'
	ABANDONED = 'ABANDONED'


class AccountsUsersUserFavoriteFilterSorting(str, Enum):
	CREATED_AT_DESC = 'CREATED_AT_DESC'
	CREATED_AT_ASC = 'CREATED_AT_ASC'
	FRESH_AT_DESC = 'FRESH_AT_DESC'
	FRESH_AT_ASC = 'FRESH_AT_ASC'
	RATING_DESC = 'RATING_DESC'
	RATING_ASC = 'RATING_ASC'
	YEAR_DESC = 'YEAR_DESC'
	YEAR_ASC = 'YEAR_ASC'
