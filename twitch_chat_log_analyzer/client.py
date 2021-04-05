from .api import TwitchAPI


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
            self._token = self.get_twitch_oauth_token(self.client_id, self.client_secret)
        return self._token

    @property
    def headers(self):
        return {
            "Client-ID": f"{self.client_id}",
            "Authorization": f"Bearer {self.token}",
        }
