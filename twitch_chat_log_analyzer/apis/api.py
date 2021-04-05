"""This module is an interface between the latest Twitch API and the user"""
import requests

from .base_api import BaseAPI


class TwitchAPI(BaseAPI):
    base_twitch_url = "https://api.twitch.tv/helix"

    @staticmethod
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

    def search_channels(self, query):
        url = f"{self.base_twitch_url}/search/channels"
        params = {
            "query": query,
        }

        return self._handle_call("GET", url, params=params).json()

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
            print(ids)
            print(user_id)
            print(game_id)
            print(optional_query_params)
            raise Exception("Missing required query param: (ids, user_id, or game_id)")

        url = f"{self.base_twitch_url}/videos"

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

        return self._handle_call("GET", url, params=params).json()

    def get_games(
        self, game_id=None, name=None, **optional_query_params
    ):

        url = f"{self.base_twitch_url}/games"

        params = {**optional_query_params}

        if game_id:
            params["id"] = game_id

        if name:
            params["name"] = name

        return self._handle_call("GET", url, params=params).json()

    def get_clips(
        self, broadcaster_id=None, game_id=None, clip_ids=None, **optional_query_params
    ):
        """Gets clip information by clip ID (one or more),
            broadcaster ID (one only), or game ID (one only).

        The response has a JSON payload with a data field containing
        an array of clip information elements and a pagination field
        containing information required to query for more streams.

        https://dev.twitch.tv/docs/api/reference#get-clips

        Args:
            broadcaster_id (str): ID of the broadcaster for whom clips are returned.
                The number of clips returned is determined by
                the first query-string parameter (default: 20).
                Results are ordered by view count.
            game_id (str): ID of the game for which clips are returned.
                The number of clips returned is determined by
                the first query-string parameter (default: 20).
                Results are ordered by view count.
            clip_id (List[str]): ID of the clip being queried. Limit: 100.
        """
        url = f"{self.base_twitch_url}/clips"

        params = {**optional_query_params}

        if broadcaster_id:
            params["broadcaster_id"] = broadcaster_id

        if game_id:
            params["game_id"] = game_id

        if clip_ids:
            clip_id_str = ",".join(clip_ids)
            params["id"] = clip_id_str

        return self._handle_call("GET", url, params=params).json()
