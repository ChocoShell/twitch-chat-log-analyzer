import os

from .api import TwitchAPI
from .json_utils import write_json_file


class TwitchClientv5(TwitchAPI):
    def __init__(self, client_id):
        self.headers = {"Client-id": client_id}

    def get_chat_for_video(self, video_id, cursor=None):
        url = f"https://api.twitch.tv/v5/videos/{video_id}/comments"

        params = {}
        if cursor is not None:
            params["cursor"] = cursor

        return self.twitch_api("GET", url, params=params)

    def download_vod_chat(self, video_ids, download_dir="./", verbose=True):
        if verbose:
            video_len = len(video_ids)
            print(f"Downloading {video_len} chats")
            count = 0

        for video_id in video_ids:
            try:
                if verbose:
                    count += 1
                    print(f"Downloading {count}/{video_len}")
                new_comments_dir = os.path.join(download_dir, video_id)
                new_comments_dir_partial = os.path.join(
                    download_dir, video_id, "partial"
                )
                try:
                    os.mkdir(new_comments_dir)
                except FileExistsError:
                    pass
                try:
                    os.mkdir(new_comments_dir_partial)
                except FileExistsError:
                    pass
                complete_comments_data = self.fetch_all(
                    lambda cursor: self.get_chat_for_video(video_id, cursor=cursor),
                    lambda index: f"{new_comments_dir_partial}/comments_{index}.json",
                    lambda data: data["comments"],
                    lambda data: data["_next"],
                )
                write_json_file(
                    complete_comments_data, f"{new_comments_dir}/comments.json"
                )
            except Exception as err:
                print(err)

    @staticmethod
    def fetch_all(api_function, file_format, get_data, get_updator, updator=None):
        fetch = True
        complete_data = []
        index = 0
        while fetch:
            data = api_function(updator)
            write_json_file(data, file_format(index))

            complete_data += get_data(data)
            index += 1
            try:
                updator = get_updator(data)
            except Exception:
                fetch = False
        return complete_data
