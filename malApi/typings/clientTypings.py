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
