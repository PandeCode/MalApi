# MalApi

## Instructions

-   Create an app at https://myanimelist.net/apiconfig (May want to use http://localhost:8000/callback)
-   Place the MAL_CLIENT_ID, MAL_CLIENT_SECRECT and MAL_REDIRECT_URI in the .env file (Refer .env.safe).

## Example

```python
#!/bin/env python3
from pprint import pprint
from pathlib import Path

from mal_api.client import Client
from mal_api.auth import Auth

MAL_CLIENT_ID     = "MAL_CLIENT_ID"
MAL_CLIENT_SECRET = "MAL_CLIENT_SECRECT"
MAL_REDIRECT_URI  = "http://127.0.0.1:8000/callback"

def main():
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
```
