#!/bin/env python3

import os
import requests

from .auth import Auth
from .typings.userAnimeList import UserAnimeList
from .typings.userData import UserData
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint
from typing import Literal, Union


load_dotenv()

# max limit = 1000

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


class Client:
	BASE_URL = "https://api.myanimelist.net/v2/"

	def __init__(self, auth: Auth) -> None:
		self.auth = auth

	# Anime
	def getAnimeList(
		self, query: str, limit: int = 100, offset: int = 0, fields: Union[None, str] = None
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getAnimeDetails(self, animeId: int, fields: Union[None, str] = None):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getAnimeRanking(
		self,
		rankingType: str,
		limit: int = 100,
		offset: int = 0,
		fields: Union[None, str] = None,
	):
		"""
The returned anime contains the ranking field.
ranking_type:
all          Top Anime Series
airing       Top Airing Anime
upcoming     Top Upcoming Anime
tv           Top Anime TV Series
ova          Top Anime OVA Series
movie        Top Anime Movies
special      Top Anime Specials
bypopularity Top Anime by Popularity
favorite     Top Favorited Anime
        """
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getSeasonalAnime(
		self,
		year: int,
		season: str,
		limit: int = 100,
		offset: int = 0,
		fields: Union[None, str] = None,
	):
		"""
sort
	anime_score          Descending
	anime_num_list_users Descending

	Season name Months
	winter      January, February, March
	spring      April, May, June
	summer      July, August, September
	fall        October, November, December
		"""
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	# User Anime

	def getUserSuggestedAnime(
		self, limit: int = 100, offset: int = 0, fields: Union[None, str] = None
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def updateUserStatusList(self, animeId: int):
		"""
REQUEST BODY SCHEMA: application/x-www-form-urlencoded
status   string: [watching | completed | on_hold | dropped | plan_to_watch]
is_rewatching  boolean
score integer 0-10
num_watched_episodes integer
priority integer 0-2
num_times_rewatched integer
rewatch_value integer 0-5
tags string
comments string
"""
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def deleteUserAnime(self, animeId: int):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getUserAnimeList(self, userName: str = "@me", limit: int = 100) -> UserAnimeList:
		"""
status: Union[None | "watching" | "completed" | "on_hold" | "dropped" | "plan_to_watch"]

sort:
Value	Order
list_score	Descending
list_updated_at	Descending
anime_title	Ascending
anime_start_date	Descending
anime_id (Under Development)	Ascending
		"""
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"users/{userName}/animelist?fields=list_status&limit={limit}"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}

		res = requests.get(url, headers=headers)
		return res.json()

	# Forums

	def getForumBoards(self):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getForumTopicDetail(self, topicId: int, limit: int = 100, offset: int = 0):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getForumTopics(
		self,
		boardId: int,
		subboardId: int,
		limit: int = 100,
		sort: str = "recent",
		q: Union[str, None] = None,
		topicUserName: Union[str, None] = None,
		userName: Union[str, None] = None,
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	# Manga
	def getMangaList(
		self, q: str, limit: int = 100, offset: int = 0, fields: Union[None, str] = None
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getMangaDetails(self, mangaId: str, fields: Union[None, str] = None):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getMangaRanking(
		self,
		rankingType: MangaRankingType = "all",
		limit: int = 100,
		offset: int = 0,
		fields: Union[None, str] = None,
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	# User Manga

	def updateUserMangaListStatus(
		self,
		mangaId: int,
		status: MangaStatus,
		isReReading: bool,
		score: int,
		numVolsRead: int,
		numChaptersRead: int,
		priority: int,
		numTimesRead: int,
		reReadValue: int,
		tags: str,
		comments: str,
	):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def deleteUserMangaListItem(self, mangaId: int):
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	def getUserMangaList(
		self,
		mangaId: int,
		status: MangaStatus,
		sort: MangaSortVaildValues,
		limit: int = 100,
		offset: int = 0,
	):
		"""
sort	
string
Valid values:

	Value	Order
	list_score	Descending
	list_updated_at	Descending
	manga_title	Ascending
	manga_start_date	Descending
	manga_id (Under Development)	Ascending
		"""
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")
		raise NotImplementedError()
		# TODO: Implement
		# TODO: Document

	# User
	def getUserData(self, userName: str = "@me") -> UserData:
		# TODO: Document
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"users/{userName}?fields=anime_statistics"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}

		res = requests.get(url, headers=headers)
		return res.json()


def __main():
	MAL_CLIENT_ID = os.getenv("MAL_CLIENT_ID")
	MAL_CLIENT_SECRET = os.getenv("MAL_CLIENT_SECRET")
	MAL_REDIRECT_URI = os.getenv("MAL_REDIRECT_URI")

	if not MAL_CLIENT_ID or not MAL_CLIENT_SECRET or not MAL_REDIRECT_URI:
		raise Exception("Environment Variables not loaded")

	auth = Auth(
		clientId=MAL_CLIENT_ID,
		clientSecret=MAL_CLIENT_SECRET,
		redirectUri=MAL_REDIRECT_URI,
		cacheFile=Path.joinpath(Path.home(), ".cache/malCache.json"),
	)

	auth.authenticate()

	client = Client(auth=auth)
	pprint(client.getUserData())
	pprint(client.getUserAnimeList(limit=10))


if __name__ == "__main__":
	__main()
