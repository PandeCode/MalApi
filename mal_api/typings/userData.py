from typing import TypedDict


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


if __name__ == "__main__":
	data: UserData = {
		"anime_statistics": {
			"mean_score": 7.46,
			"num_days": 20.85,
			"num_days_completed": 13.13,
			"num_days_dropped": 0,
			"num_days_on_hold": 4.45,
			"num_days_watched": 25.34,
			"num_days_watching": 3.27,
			"num_episodes": 1629,
			"num_items": 170,
			"num_items_completed": 77,
			"num_items_dropped": 0,
			"num_items_on_hold": 6,
			"num_items_plan_to_watch": 76,
			"num_items_watching": 11,
			"num_times_rewatched": 0,
		},
		"birthday": "2000-09-02",
		"id": 13295048,
		"joined_at": "2021-07-14T19:41:28+00:00",
		"location": "",
		"name": "d3bug64",
	}
