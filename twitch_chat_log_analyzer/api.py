from .base_api import BaseAPI


class TwitchAPI(BaseAPI):
    base_twitch_url = "https://api.twitch.tv/helix"

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
