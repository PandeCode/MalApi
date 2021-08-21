from typing import TypedDict, Optional


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


if __name__ == "__main__":
	data: UserAnimeList = {
		"data": [
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 1,
					"score": 8,
					"start_date": "2021-08-03",
					"status": "plan_to_watch",
					"updated_at": "2021-08-05T08:19:02+00:00",
				},
				"node": {
					"id": 38101,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/1819/97947l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/1819/97947.jpg",
					},
					"title": "5-toubun no Hanayome",
				},
			},
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 12,
					"score": 7,
					"start_date": "2021-08-03",
					"status": "completed",
					"updated_at": "2021-08-03T19:30:49+00:00",
				},
				"node": {
					"id": 39790,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/1649/109056l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/1649/109056.jpg",
					},
					"title": "Adachi to Shimamura",
				},
			},
			{
				"list_status": {
					"is_rewatching": False,
					"num_episodes_watched": 1,
					"score": 7,
					"status": "plan_to_watch",
					"updated_at": "2021-08-05T08:22:57+00:00",
				},
				"node": {
					"id": 34881,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/7/86665l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/7/86665.jpg",
					},
					"title": "Aho Girl",
				},
			},
			{
				"list_status": {
					"is_rewatching": False,
					"num_episodes_watched": 1,
					"score": 7,
					"status": "plan_to_watch",
					"updated_at": "2021-08-05T08:19:02+00:00",
				},
				"node": {
					"id": 22199,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/1429/95946l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/1429/95946.jpg",
					},
					"title": "Akame ga Kill!",
				},
			},
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 1,
					"score": 7,
					"start_date": "2021-08-03",
					"status": "plan_to_watch",
					"updated_at": "2021-08-05T08:19:02+00:00",
				},
				"node": {
					"id": 36882,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/1776/97682l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/1776/97682.jpg",
					},
					"title": "Arifureta Shokugyou de Sekai Saikyou",
				},
			},
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 139,
					"score": 10,
					"start_date": "2021-08-03",
					"status": "watching",
					"updated_at": "2021-08-18T22:44:42+00:00",
				},
				"node": {
					"id": 34572,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/2/88336l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/2/88336.jpg",
					},
					"title": "Black Clover",
				},
			},
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 25,
					"score": 8,
					"start_date": "2021-08-03",
					"status": "completed",
					"updated_at": "2021-08-03T19:30:49+00:00",
				},
				"node": {
					"id": 33486,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/12/85221l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/12/85221.jpg",
					},
					"title": "Boku no Hero Academia 2nd Season",
				},
			},
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 25,
					"score": 8,
					"start_date": "2021-08-03",
					"status": "completed",
					"updated_at": "2021-08-03T19:30:49+00:00",
				},
				"node": {
					"id": 36456,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/1319/92084l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/1319/92084.jpg",
					},
					"title": "Boku no Hero Academia 3rd Season",
				},
			},
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 25,
					"score": 8,
					"start_date": "2021-08-03",
					"status": "completed",
					"updated_at": "2021-08-03T19:30:49+00:00",
				},
				"node": {
					"id": 38408,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/1412/107914l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/1412/107914.jpg",
					},
					"title": "Boku no Hero Academia 4th Season",
				},
			},
			{
				"list_status": {
					"finish_date": "2021-08-03",
					"is_rewatching": False,
					"num_episodes_watched": 18,
					"score": 10,
					"start_date": "2021-08-03",
					"status": "watching",
					"updated_at": "2021-08-14T12:25:01+00:00",
				},
				"node": {
					"id": 41587,
					"main_picture": {
						"large": "https://api-cdn.myanimelist.net/images/anime/1911/113611l.jpg",
						"medium": "https://api-cdn.myanimelist.net/images/anime/1911/113611.jpg",
					},
					"title": "Boku no Hero Academia 5th Season",
				},
			},
		],
		"paging": {
			"next": "https://api.myanimelist.net/v2/users/@me/animelist?offset=10&fields=list_status&limit=10"
		},
	}
