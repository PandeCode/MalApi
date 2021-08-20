#!/bin/env python3

import os
import requests

from .auth import Auth
from .typings.userAnimeList import UserAnimeList
from .typings.userData import UserData
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint


load_dotenv()


class Client:
	BASE_URL = "https://api.myanimelist.net/v2/"

	def __init__(self, auth: Auth) -> None:
		self.auth = auth

	def getUserData(self, userName: str = "@me") -> UserData:
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"users/{userName}?fields=anime_statistics"
		headers = {"Authorization": f"Bearer {self.auth.authData[ 'access_token' ]}"}

		res = requests.get(url, headers=headers)
		return res.json()

	def getUserAnimeList(self, userName: str = "@me", limit: int = 4) -> UserAnimeList:
		if not self.auth.authData:
			raise Exception("Auth data is None. Run auth.authenticate() before use.")

		url = self.BASE_URL + f"users/{userName}/animelist?fields=list_status&limit={limit}"
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
