import requests


class TwitchAPIv5:
    base_twitch_url = "https://api.twitch.tv/kraken"

    def get_chat_for_video(self, client_id, video_id, cursor=None):
        """Get VOD Chat

        Args:
            client_id (str): client id for authorization
            video_id (str): Twitch VOD id
            cursor (str, optional): The pagination cursor of where to pick up from. Defaults to None.

        Raises:
            err: Error raised during Response

        Returns:
            response: Response Object
        """

        headers = {"Client-ID": client_id}

        url = f"https://api.twitch.tv/v5/videos/{video_id}/comments"

        params = {}
        if cursor is not None:
            print(f"Downloading log for {video_id} at cursor: {cursor}")
            params["cursor"] = cursor
        else:
            print(f"Downloading log for {video_id} with no cursor")

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
        except Exception as err:
            raise err

        return response

    def get_clip(self, client_id, slug):
        """Get Clip data for given slug

        Args:
            client_id (str): client ID for authorization
            slug (str): Globally unique string

        Raises:
            err: returns on request errors

        Returns:
            response: successful response object
        """
        url = f"{self.base_twitch_url}/clips/{slug}"

        headers = {
            "Accept": "application/vnd.twitchtv.v5+json",
            "Client-ID": client_id
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except Exception as err:
            raise err

        return response
