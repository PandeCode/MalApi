#!/bin/env python3
import os
from pprint import pprint
from pathlib import Path

from mal_api.client import Client
from mal_api.auth import Auth


def main():
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
	pprint(client.getUserAnimeList())


if __name__ == "__main__":
	main()
