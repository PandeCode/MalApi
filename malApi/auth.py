#!/bin/env python3

import os
from pathlib import Path
import requests
from pprint import pprint
import secrets
from .listener import getCode
import json
from typing import TypedDict, Union

import webbrowser
from dotenv import load_dotenv

load_dotenv()


class AuthData(TypedDict):
	token_type: str
	expires_in: int
	access_token: str
	refresh_token: str


class Auth:
	def __init__(
		self,
		clientId: str,
		clientSecret: str,
		redirectUri: str,
		state: str = "RequestForToken",
		cacheFile: Union[str, Path] = "./cache.json",
	) -> None:
		self.CLIENT_ID = clientId
		self.CLIENT_SECRET = clientSecret
		self.REDIRECT_URI = redirectUri

		self.STATE = state
		self.CODE_CHALLENGE = self.getNewCodeVerifier()
		self.AUTH_URL = (
			"https://myanimelist.net/v1/oauth2/authorize"
			f"?response_type=code"
			f"&client_id={self.CLIENT_ID}"
			f"&code_challenge={self.CODE_CHALLENGE}"
			f"&state={self.STATE}"
			f"&redirect_uri={self.REDIRECT_URI}"
		)

		self.cacheFile = Path(cacheFile)
		self.isAuthenticated = False
		self.authData: Union[None, AuthData] = None

	def getCache(self):
		try:
			if self.cacheFile.exists():
				with open(self.cacheFile) as file:
					self.authData = json.loads(file.read())
				if not self.authData or not self.authData["token_type"]:
					self.authData = None
					return False
			else:
				with open(self.cacheFile, "w+") as file:
					file.write("{}")
				self.authData = None
				return False
		except:
			self.authData = None
			return False

		return True

	def expired(self) -> bool:
		if not self.authData:
			return True

		url = "https://api.myanimelist.net/v2/users/@me"
		headers = {"Authorization": f"Bearer {self.authData['access_token']}"}

		res = requests.get(url, headers=headers)

		return False if res.status_code == 200 else True

	def authenticate(self):
		self.getCache()
		if not self.expired():
			return

		if not self.authData:
			webbrowser.open_new_tab(self.AUTH_URL)

			code = self.listenForAuthCode()
			if not code:
				raise Exception("Problem listening for auth code.")

			data = self.getToken(code)
			if not data:
				raise Exception("Problem getting auth data.")
			self.authData = data
		else:
			if not self.authData or not self.authData["token_type"]:
				raise Exception("Problem getting auth data.")
			self.authData = self.getNewToken()

		with open(self.cacheFile, "w+") as file:
			json.dump(self.authData, file)

		self.isAuthenticated = True

	def getToken(self, code: str):
		baseUrl = "https://myanimelist.net/v1/oauth2/token"
		headers = {"Content-Type": "application/x-www-form-urlencoded"}
		data = {
			"client_id": self.CLIENT_ID,
			"client_secret": self.CLIENT_SECRET,
			"code": code,
			"code_verifier": self.CODE_CHALLENGE,
			"grant_type": "authorization_code",
			"redirect_uri": self.REDIRECT_URI,
		}
		response = requests.post(baseUrl, data=data, headers=headers,)
		response.raise_for_status()

		return response.json()

	def getNewToken(self):
		if not self.authData:
			raise Exception("No Auth data or refresh_token")
		if not self.authData["refresh_token"]:
			raise Exception("No Auth data")

		baseUrl = "https://myanimelist.net/v2/oauth2/token"
		headers = {"Content-Type": "application/x-www-form-urlencoded"}
		data = {
			"client_id": self.CLIENT_ID,
			"client_secret": self.CLIENT_SECRET,
			"grant_type": "refresh_token",
			"redirect_uri": self.REDIRECT_URI,
			"refresh_token": self.authData["refresh_token"],
		}
		response = requests.post(baseUrl, data=data, headers=headers,)
		response.raise_for_status()

		return response.json()

	@staticmethod
	def listenForAuthCode() -> str:
		code = getCode()

		if not code:
			raise Exception("No output")

		return code

	@staticmethod
	def getNewCodeVerifier() -> str:
		token = secrets.token_urlsafe(100)
		return token[:128]


if __name__ == "__main__":
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
