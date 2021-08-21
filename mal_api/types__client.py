from typing import TypedDict, Optional
from typing import Literal, Union

MangaRankingType = Union[
	Literal["all"],
	Literal["manga"],
	Literal["oneshots"],
	Literal["doujin"],
	Literal["lightnovels"],
	Literal["novels"],
	Literal["manhwa"],
	Literal["manhua"],
	Literal["bypopularity"],
	Literal["favorite"],
]

MangaStatus = Union[
	Literal["reading"],
	Literal["completed"],
	Literal["on_hold"],
	Literal["dropped"],
	Literal["plan_to_read"],
]

MangaSortVaildValues = Union[
	Literal["list_score"],
	Literal["list_updated_at"],
	Literal["manga_title"],
	Literal["manga_start_date"],
]

AnimeStatus = Union[
	Literal["watching"],
	Literal["completed"],
	Literal["on_hold"],
	Literal["dropped"],
	Literal["plan_to_watch"],
]

AnimeRankType = Union[
	Literal["all"],
	Literal["airing"],
	Literal["upcoming"],
	Literal["tv"],
	Literal["ova"],
	Literal["movie"],
	Literal["special"],
	Literal["bypopularity"],
	Literal["favorite"],
]

UserAnimeSortVaildValues = Union[
	Literal["list_score"],
	Literal["list_updated_at"],
	Literal["anime_title"],
	Literal["anime_start_date"],
]
AnimeSeasonSort = Union[
	Literal["anime_score"], Literal["anime_num_list_users"],
]

AnimeSeason = Union[
	Literal["winter"], Literal["spring"], Literal["summer"], Literal["fall"],
]


class AnimeDataNodeMainPicture(TypedDict):
	medium: str  # JPEG URL
	large: str  # JPEG URL


class AnimeDataNode(TypedDict):
	id: int
	title: str
	main_picture: AnimeDataNodeMainPicture


class AnimeDataListStatus(TypedDict, total=False):
	finish_date: Optional[str]  # datetime
	start_date: Optional[str]  # datetime

	status: str
	score: int
	num_episodes_watched: int
	is_rewatching: bool
	updated_at: str  # datetime


class AnimeData(TypedDict):
	node: AnimeDataNode
	list_status: AnimeDataListStatus


class Paging(TypedDict, total=False):
	next: Optional[str]  # url
	previous: Optional[str]  # url


class UserAnimeList(TypedDict):
	data: list[AnimeData]
	paging: Paging


class UserAnimeStatistics(TypedDict):
	mean_score: float
	num_days: float
	num_days_completed: float
	num_days_dropped: float
	num_days_on_hold: float
	num_days_watched: float
	num_days_watching: float
	num_episodes: int
	num_items: int
	num_items_completed: int
	num_items_dropped: int
	num_items_on_hold: int
	num_items_plan_to_watch: int
	num_items_watching: int
	num_times_rewatched: int


class UserData(TypedDict, total=False):
	id: int
	name: str
	location: str
	joined_at: str
	birthday: str  # Date
	anime_statistics: UserAnimeStatistics
