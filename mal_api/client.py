#!/bin/env python3

import requests

from .auth import Auth
from .types__client import (
	AnimeSeason,
	AnimeSeasonSort,
	MangaRankingType,
	MangaStatus,
	MangaSortVaildValues,
	AnimeRankType,
	AnimeStatus,
	UserAnimeSortVaildValues,
	UserData,
	UserAnimeList,
)
from typing import Union, Literal


class Client:
	BASE_URL = "https://api.myanimelist.net/v2/"

	def __init__(self, auth: Auth) -> None:
		self.auth = auth

	# Anime
	def getAnimeList(
		self, query: str, limit: int = 100, offset: int = 0, fields: Union[None, str] = None
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + "anime"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params = {"q": query, "limit": limit, "offset": offset, "fields": fields}
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	def getAnimeDetails(self, animeId: int, fields: Union[None, str] = None):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"anime/{animeId}"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params: dict[str, str] = {}
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	def getAnimeRanking(
		self,
		rankingType: AnimeRankType = "all",
		limit: int = 100,
		offset: int = 0,
		fields: Union[None, str] = None,
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + "anime/ranking"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params: dict[str, Union[str, int]] = {"limit": limit, "offset": offset}
		if rankingType:
			params["ranking_type"] = rankingType
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	def getSeasonalAnime(
		self,
		year: int,
		season: AnimeSeason,
		sort: Union[None, AnimeSeasonSort,] = None,
		limit: int = 100,
		offset: int = 0,
		fields: Union[None, str] = None,
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"anime/season/{year}/{season}"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params: dict[str, Union[str, int]] = {"limit": limit, "offset": offset}
		if sort:
			params["sort"] = sort
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	# User Anime

	def getUserSuggestedAnime(
		self, limit: int = 100, offset: int = 0, fields: Union[None, str] = None
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		url = self.BASE_URL + "anime/suggestions"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params: dict[str, Union[str, int]] = {"limit": limit, "offset": offset}
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	def updateUserAnimeListStatus(
		self,
		animeId: int,
		status: Union[None, AnimeStatus] = None,
		score: Union[None, int] = None,
		priority: Union[None, int] = None,
		numWatchedEpisodes: Union[None, int] = None,
		isRewatching: Union[None, bool] = None,
		numTimesRewatched: Union[None, int] = None,
		rewatchValue: Union[None, int] = None,
		tags: Union[None, str] = None,
		comments: Union[None, str] = None,
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"anime/{animeId}/my_list_status"
		headers = {
			"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}",
			"Content-Type": "application/x-www-form-urlencoded",
		}
		data: dict[str, Union[str, int]] = {}

		if status:
			data["status"] = status
		if score:
			data["score"] = score
		if priority:
			data["priority"] = priority
		if tags:
			data["tags"] = tags
		if comments:
			data["comments"] = comments
		if numWatchedEpisodes:
			data["num_watched_episodes"] = numWatchedEpisodes
		if isRewatching:
			data["is_rewatching"] = isRewatching
		if numTimesRewatched:
			data["num_times_rewatched"] = numTimesRewatched
		if rewatchValue:
			data["rewatch_value"] = rewatchValue

		res = requests.patch(url, data=data, headers=headers)
		return res.json()

	def deleteUserAnime(self, animeId: int):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		url = self.BASE_URL + f"anime/{animeId}/my_list_status"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		res = requests.delete(url, headers=headers)
		return res.status_code

	def getUserAnimeList(
		self,
		userName: str = "@me",
		limit: int = 100,
		offset: int = 0,
		status: Union[AnimeStatus, None] = None,
		sort: Union[UserAnimeSortVaildValues, None] = None,
	) -> UserAnimeList:

		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"users/{userName}/animelist"
		params = {"field": "list_status", "limit": limit, "offset": offset}
		if status:
			params["status"] = status
		if sort:
			params["sort"] = sort
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	# Forums

	def getForumBoards(self):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + "forum/boards"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}

		res = requests.get(url, headers=headers)

		res.raise_for_status()

		return res.json()

	def getForumTopicDetail(self, topicId: int, limit: int = 100, offset: int = 0):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"forum/topic/{topicId}"
		params = {"limit": limit, "offset": offset}
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	def getForumTopics(
		self,
		boardId: Union[int, None] = None,
		subboardId: Union[int, None] = None,
		limit: int = 100,
		offset: int = 0,
		sort: Union[Literal["recent"], None] = None,
		query: Union[str, None] = None,
		topicUserName: Union[str, None] = None,
		userName: Union[str, None] = None,
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + "forum/topics"
		params: dict[str, Union[int, str]] = {"limit": limit, "offset": offset}
		if boardId:
			params["board_id"] = boardId
		if subboardId:
			params["subboard_id"] = subboardId
		if sort:
			params["sort"] = sort
		if query:
			params["q"] = query
		if topicUserName:
			params["topic_user_name"] = topicUserName
		if userName:
			params["user_name"] = userName

		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	# Manga
	def getMangaList(
		self, query: str, limit: int = 100, offset: int = 0, fields: Union[None, str] = None
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + "manga"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params = {"q": query, "limit": limit, "offset": offset, "fields": fields}
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	def getMangaDetails(self, mangaId: int, fields: Union[None, str] = None):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"manga/{mangaId}"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params: dict[str, str] = {}
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	def getMangaRanking(
		self,
		rankingType: MangaRankingType = "all",
		limit: int = 100,
		offset: int = 0,
		fields: Union[None, str] = None,
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + "manga/ranking"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		params: dict[str, Union[str, int]] = {"limit": limit, "offset": offset}
		if rankingType:
			params["ranking_type"] = rankingType
		if fields:
			params["fields"] = fields

		res = requests.get(url, headers=headers, params=params)

		res.raise_for_status()

		return res.json()

	# User Manga

	def updateUserMangaListStatus(
		self,
		mangaId: int,
		status: Union[None, MangaStatus] = None,
		isReReading: Union[None, bool] = None,
		score: Union[None, int] = None,
		numVolsRead: Union[None, int] = None,
		numChaptersRead: Union[None, int] = None,
		priority: Union[None, int] = None,
		numTimesRead: Union[None, int] = None,
		reReadValue: Union[None, int] = None,
		tags: Union[None, str] = None,
		comments: Union[None, str] = None,
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"manga/{mangaId}/my_list_status"
		headers = {
			"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}",
			"Content-Type": "application/x-www-form-urlencoded",
		}
		data: dict[str, Union[str, int]] = {}

		if status:
			data["status"] = status
		if isReReading:
			data["is_rereading"] = isReReading
		if score:
			data["score"] = score
		if numVolsRead:
			data["num_vols_read"] = numVolsRead
		if numChaptersRead:
			data["num_chapters_read"] = numChaptersRead
		if priority:
			data["priority"] = priority
		if numTimesRead:
			data["num_times_read"] = numTimesRead
		if reReadValue:
			data["reread_value"] = reReadValue
		if tags:
			data["tags"] = tags
		if comments:
			data["comments"] = comments
		res = requests.patch(url, data=data, headers=headers)
		return res.json()

	def deleteUserMangaListItem(self, mangaId: int):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		url = self.BASE_URL + f"manga/{mangaId}/my_list_status"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		res = requests.delete(url, headers=headers)
		return res.status_code

	def getUserMangaList(
		self,
		userName: str = "@me",
		status: Union[MangaStatus, None] = None,
		sort: Union[MangaSortVaildValues, None] = None,
		limit: int = 100,
		offset: int = 0,
	):
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		url = self.BASE_URL + f"users/{userName}/mangalist"
		params = {"field": "list_status", "limit": limit, "offset": offset}
		if status:
			params["status"] = status
		if sort:
			params["sort"] = sort
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		res = requests.get(url, headers=headers, params=params)
		res.raise_for_status()
		return res.json()

	# User
	def getUserData(
		self, userName: str = "@me", fields: Union[None, str] = None,
	) -> UserData:
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		url = self.BASE_URL + f"users/{userName}"
		params: dict[str, str] = {}
		if fields:
			params["fields"] = fields
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}
		res = requests.get(url, headers=headers, params=params)
		res.raise_for_status()
		return res.json()
