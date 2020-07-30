import requests

from .api import TwitchAPI


base_twitch_url = "https://api.twitch.tv/helix/"


class TwitchClient(TwitchAPI):
    """
    Client to connect to Twitch API from April 30, 2020 and manage OAuth

    https://dev.twitch.tv/docs/api/reference

    Attrs:
        client_id (str)
        client_secret (str)
        token (str): OAuth Access Token
        headers (dict): headers dictionary for Twitch API requests

    Methods:
        search_channels(query): Returns channel search results for given query
        get_videos(
            ids=None, user_id=None, game_id=None, **optional_query_params
        ): Returns list of video metadata for given search parameters
    """
    def __init__(self, client_id, client_secret):
        """Stores client credentials and internal token parameter

        Args:
            client_id ([type]): [descripti (])on
            client_secret ([type]): [descripti (])on
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._token = None

    @property
    def token(self):
        if self._token is None:
            self._token = get_twitch_oauth_token(self.client_id, self.client_secret)
        return self._token

    @property
    def headers(self):
        return {
            "Client-ID": f"{self.client_id}",
            "Authorization": f"Bearer {self.token}",
        }

    def search_channels(self, query):
        url = f"{base_twitch_url}search/channels"
        params = {
            "query": query,
        }

        return self.twitch_api("GET", url, params=params)

    def get_videos(self, ids=None, user_id=None, game_id=None, **optional_query_params):
        """Get list of video metadata

        Args:
            ids (List[str], optional): List of video ID numbers as strings. Defaults to None.
            user_id (str, optional): User ID to pull videos from. Defaults to None.
            game_id (str, optional): Game ID to pull videos from. Defaults to None.

        Raises:
            Exception: Raised when all args are None

        Returns:
            List[dict]: List of dictionaries containing video metadata
        """
        if ids is None and user_id is None and game_id is None:
            raise Exception("Missing required query param: (ids, user_id, or game_id)")

        url = f"{base_twitch_url}videos"

        params = {**optional_query_params}

        if ids is not None:
            if isinstance(ids, str):
                params["id"] = ids
            else:
                params["id"] = ",".join(ids)

        if user_id is not None:
            params["user_id"] = user_id

        if game_id is not None:
            params["game_id"] = game_id

        return self.twitch_api("GET", url, params=params)


def get_twitch_oauth_token(client_id, client_secret):
    """Get Twitch Access Token

    Args:
        client_id (str)
        client_secret (str):

    Returns:
        (str): OAuth Access Token
    """
    params = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    twitch_oauth_url = "https://id.twitch.tv/oauth2/token"

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        response = requests.post(twitch_oauth_url, headers=headers, params=params)
        response.raise_for_status()
    except Exception as err:
        print(err)
        raise err

    return response.json()["access_token"]
