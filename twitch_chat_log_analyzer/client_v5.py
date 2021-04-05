import os

from .apis.api_v5 import TwitchAPIv5
from .json_utils import write_json_file, load_json_file


class TwitchClientv5:
    def __init__(self, client_id):
        self.client_id = client_id
        self.api = TwitchAPIv5()

    def combine_vod_chat_json_files(self, filelist):
        for file in filelist:
            _ = load_json_file(file)

    def download_complete_vod_chat_in_parts(
        self, video_id, download_dir="./", filename=None
    ):
        vod_chat_generator = self.get_complete_vod_chat(video_id)

        for i, chat_page in enumerate(vod_chat_generator):
            filepath = os.path.join(download_dir, f"comments_{video_id}_{i}.json")
            write_json_file(chat_page.json(), filepath)
            yield filepath

    def get_complete_vod_chat_in_parts(self, video_id):
        data = self.api.get_chat_for_video(self.client_id, video_id).json()
        cursor = data.get("_next")
        yield data

        while cursor:
            data = self.api.get_chat_for_video(
                self.client_id, video_id, cursor=cursor
            ).json()
            cursor = data.get("_next")
            yield data

    def download_complete_vods_chat(self, video_ids, download_dir="./", verbose=True):
        """Downloads complete chat by looping through the pagination cursor until end
        of a list of VOD IDs then writes chat to file into a directory.

        Args:
            video_ids ([type]): [description]
            download_dir (str, optional): [description]. Defaults to "./".
            verbose (bool, optional): [description]. Defaults to True.
        """
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
                    lambda cursor: self.api.get_chat_for_video(
                        self.client_id, video_id, cursor=cursor
                    ).json(),
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
    def fetch_all(get_data, get_filename, format_data, get_next, updator=None):
        """While get_next continues to return valid value, run get_data on next
        value. Then write this data to a new function determined by get_filename.
        Then return the formatted data back.

        Args:
            get_data (func): Gets data given updator
            get_filename (func): Gets filename to write data to
            format_data (func): format data for
            get_next (func): [description]
            updator (Any, optional): [description]. Defaults to None.

        Returns:
            [type]: [description]
        """
        fetch = True
        complete_data = []
        index = 0
        while fetch:
            data = get_data(updator)
            write_json_file(data, get_filename(index))

            complete_data += format_data(data)
            index += 1
            try:
                updator = get_next(data)
            except Exception:
                fetch = False
        return complete_data
