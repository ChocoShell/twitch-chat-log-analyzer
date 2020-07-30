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
