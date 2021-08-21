import os
import requests

from pprint import pprint
from pathlib import Path


from dotenv import load_dotenv

from mal_api.auth import Auth

load_dotenv()


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

	url = "https://api.myanimelist.net/v2/users/@me"
	if not auth.authData:
		raise Exception("Auth data is None")
	headers = {"Authorization": f"Bearer {auth.authData['access_token']}"}

	res = requests.get(url, headers=headers)

	print("Auth Data : ", end="")
	pprint(auth.authData)
	print("Status    : ", res.status_code)
	print("Json      : ", end="")
	pprint(res.json())


if __name__ == "__main__":
	test()
