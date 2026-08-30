# Auto-generated for enums in anime category
from enum import Enum


class AnimeCatalogFilterProductionStatus(str, Enum):
	IS_IN_PRODUCTION = 'IS_IN_PRODUCTION'
	IS_NOT_IN_PRODUCTION = 'IS_NOT_IN_PRODUCTION'


class AnimeCatalogFilterPublishStatus(str, Enum):
	IS_ONGOING = 'IS_ONGOING'
	IS_NOT_ONGOING = 'IS_NOT_ONGOING'


class AnimeCatalogFilterSorting(str, Enum):
	FRESH_AT_DESC = 'FRESH_AT_DESC'
	FRESH_AT_ASC = 'FRESH_AT_ASC'
	RATING_DESC = 'RATING_DESC'
	RATING_ASC = 'RATING_ASC'
	YEAR_DESC = 'YEAR_DESC'
	YEAR_ASC = 'YEAR_ASC'


class AnimeReleasesReleaseAgeRating(str, Enum):
	R0_PLUS = 'R0_PLUS'
	R6_PLUS = 'R6_PLUS'
	R12_PLUS = 'R12_PLUS'
	R16_PLUS = 'R16_PLUS'
	R18_PLUS = 'R18_PLUS'


class AnimeReleasesReleasePublishDay(int, Enum):
	VALUE_1 = 1
	VALUE_2 = 2
	VALUE_3 = 3
	VALUE_4 = 4
	VALUE_5 = 5
	VALUE_6 = 6
	VALUE_7 = 7


class AnimeReleasesReleaseSeason(str, Enum):
	WINTER = 'winter'
	SPRING = 'spring'
	SUMMER = 'summer'
	AUTUMN = 'autumn'


class AnimeReleasesReleaseType(str, Enum):
	TV = 'TV'
	ONA = 'ONA'
	WEB = 'WEB'
	OVA = 'OVA'
	OAD = 'OAD'
	MOVIE = 'MOVIE'
	DORAMA = 'DORAMA'
	SPECIAL = 'SPECIAL'


class AnimeReleasesReleaseMemberRole(str, Enum):
	POSTER = 'poster'
	TIMING = 'timing'
	VOICING = 'voicing'
	EDITING = 'editing'
	DECORATING = 'decorating'
	TRANSLATING = 'translating'
	HEVC = 'hevc'


class AnimeTorrentsTorrentCodec(str, Enum):
	AV1 = 'AV1'
	X264_AVC = 'x264/AVC'
	X265_HEVC = 'x265/HEVC'
	X265HQ_HEVC_HQ = 'x265hq/HEVC-HQ'


class AnimeTorrentsTorrentColor(str, Enum):
	_8BIT = '8bit'
	_10BIT = '10Bit'


class AnimeTorrentsTorrentQuality(str, Enum):
	_360P = '360p'
	_480P = '480p'
	_576P = '576p'
	_720P = '720p'
	_1080P = '1080p'
	_2K = '2k'
	_4K = '4k'
	_8K = '8k'


class AnimeTorrentsTorrentType(str, Enum):
	BDRIP = 'BDRip'
	HDRIP = 'HDRip'
	TVRIP = 'TVRip'
	WEBRIP = 'WEBRip'
	DTVRIP = 'DTVRip'
	DVDRIP = 'DVDRip'
	HDTVRIP = 'HDTVRip'
	WEB_DL = 'WEB-DL'
	WEB_DLRIP = 'WEB-DLRip'


class AnimeTorrentsTorrentMemberRole(str, Enum):
	HEVC = 'HEVC'
