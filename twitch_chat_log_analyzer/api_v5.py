from .base_api import BaseAPI


class TwitchAPIv5(BaseAPI):
    def get_chat_for_video(self, video_id, cursor=None):
        url = f"https://api.twitch.tv/v5/videos/{video_id}/comments"

        params = {}
        if cursor is not None:
            print(f"Downloading log for {video_id} at cursor: {cursor}")
            params["cursor"] = cursor
        else:
            print(f"Downloading log for {video_id} with no cursor")

        return self._handle_call("GET", url, params=params).json()
