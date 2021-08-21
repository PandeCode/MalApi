import os

from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv

from mal_api.client import Client
from mal_api.auth import Auth

load_dotenv()


def testAnime(client: Client):
	# Anime
	print('client.getAnimeList(query="Shield Hero", limit=1): ', end="")
	pprint(client.getAnimeList(query="Shield Hero", limit=1))

	print("client.getAnimeDetails(animeId=40356): ", end="")
	pprint(client.getAnimeDetails(animeId=40356))

	print('client.getAnimeRanking(rankingType="all", limit=1): ', end="")
	pprint(client.getAnimeRanking(rankingType="all", limit=1))

	print('client.getSeasonalAnime(2021, "winter", limit=1, sort="anime_score"): ', end="")
	pprint(client.getSeasonalAnime(2021, "winter", limit=1, sort="anime_score"))


def testUserAnime(client: Client):
	# User Anime
	print("client.getUserSuggestedAnime(limit=1)", end="")
	pprint(client.getUserSuggestedAnime(limit=1))

	print("client.getUserAnimeList(limit=1): ", end="")
	pprint(client.getUserAnimeList(limit=1))

	print("client.deleteUserAnime(animeId=40356): ", end="")
	pprint(client.deleteUserAnime(animeId=40356))

	print('client.updateUserAnimeListStatus(animeId=40356, status="watching"): ', end="")
	pprint(client.updateUserAnimeListStatus(animeId=40356, status="watching"))


def testForums(client: Client):
	# Forums
	print("client.getForumBoards(): ", end="")
	pprint(client.getForumBoards())

	print("client.getForumTopicDetail(topicId=14): ", end="")
	pprint(client.getForumTopicDetail(topicId=14))

	print(
		'client.getForumTopics(query="love", subboardId=1, limit=1, sort="recent"): ', end=""
	)
	pprint(client.getForumTopics(query="love", subboardId=1, limit=1, sort="recent"))


def testManga(client: Client):
	# Manga
	print('client.getMangaList(query="Shield Hero", limit=1): ', end="")
	pprint(client.getMangaList(query="Shield Hero", limit=1))

	print("client.getMangaDetails(mangaId=67615): ", end="")
	pprint(client.getMangaDetails(mangaId=67615))

	print('client.getMangaRanking(rankingType="all", limit=1): ', end="")
	pprint(client.getMangaRanking(rankingType="all", limit=1))


def testUserManga(client: Client):
	# User Manga
	print("client.getUserMangaList(): ", end="")
	pprint(client.getUserMangaList(userName="@me"))

	print('client.updateUserMangaListStatus(mangaId=67615, status="reading"): ', end="")
	pprint(client.updateUserMangaListStatus(mangaId=67615, status="on_hold"))

	print("client.deleteUserMangaListItem(mangaId=67615): ", end="")
	pprint(client.deleteUserMangaListItem(mangaId=67615))


def testUser(client: Client):
	# User
	print('client.getUserData(userName="@me", fields="anime_statistics"): ', end="")
	pprint(client.getUserData(userName="@me", fields="anime_statistics"))


def test():
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

	# testAnime(client)
	testUserAnime(client)
	# testManga(client)
	# testUserManga(client)
	# testForums(client)
	# testUser(client)


if __name__ == "__main__":
	test()
