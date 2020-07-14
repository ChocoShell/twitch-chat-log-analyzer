import os
import pandas as pd

# from twitch_chat_log_analyzer.api import TwitchClient
from twitch_chat_log_analyzer.api_v5 import TwitchClientv5
from twitch_chat_log_analyzer.models.comments import FilteredComment

from twitch_chat_log_analyzer.json_utils import write_json_file, load_json_file
from twitch_chat_log_analyzer.timestamps import (
    save_plots_from_comment_comparisons_for_search_string_from_dir,
    fetch_timestamps_from_file,
    format_timestamps,
)
from twitch_chat_log_analyzer.comments_search import write_search_results_for_ids

from twitch_chat_log_analyzer.file_utils import create_dir, find
from twitch_chat_log_analyzer.dataframes import convert_channel_comments_to_csv

creds = "creds.json"


def write_results_for_channel(channel, search_string, case_sense=True):
    comments_dir = f"./data/{channel}/comments"
    video_ids = os.listdir(comments_dir)

    directory_format = (comments_dir + "{}/comments.json").format

    write_search_results_for_ids(
        video_ids, directory_format, search_string, case_insensitive=not case_sense
    )


if __name__ == "__main__":
    convert_channel_comments_to_csv("ludwig")

    # 1. Turn json comment file to csv file
    #   - Turn json comment file to pandas dataframe
    #   - Turn json comment data into a pandas dataframe
    #   - Turn comment data into a pandas dataframe
    #   - Turn FilteredComments list into a pandas dataframe

    # --------------------
    # 1. Create credentials file for Twitch API
    # data = load_json_file(creds)
    # client_id = data["client_id"]
    # client_secret = data["client_secret"]
    # twitch_clientv5 = TwitchClientv5(client_id, client_secret)
    # twitch_client = TwitchClient(client_id, client_secret)

    # videos = load_json_file("./data/ludwig/videos/videos.json")
    # video_ids = [video["id"] for video in videos]
    # last_one = video_ids.index("621382009") + 1
    # video_ids = video_ids[last_one:]

    # twitch_clientv5.download_vod_chat(video_ids, comments_dir)

    # channel_id = "40934651"

    # archive's are past broadcasts

    search_string = "hi youtube"

    # def filter_video_id(video_id):
    #     check_file = os.path.join(comments_dir, video_id, "comments.json")
    #     return os.path.isfile(check_file)

    # video_ids = list(filter(lambda video_id: filter_video_id(video_id), video_ids))

    # format_folder_structure(video_ids, comments_dir)

    # twitch_clientv5.get_chat_for_video(video_id)

    # download_vod_chat(video_ids, download_dir=comments_path)

    # pattern = "PepoG_comments.json"
    # rename_all_matching_files(pattern, comments_dir, "PepoG_comments.json")
    # interesting_ids = [
    #     621382009,
    #     622420336,
    #     622938382,
    #     665399832,
    #     673772949,
    # ]

    # def print_timestamps_of_ids(interesting_ids, search_string):
    #     for video_id in interesting_ids:
    #         check_file = os.path.join(comments_dir, str(video_id), f"{search_string}_comments.json")
    #         timestamps = fetch_timestamps_from_file(check_file)
    #         print(video_id)
    #         print(format_timestamps(timestamps))
    #         print()

    # print_timestamps_of_ids(interesting_ids, search_string)

    # for video_id in video_ids:
    #     print(video_id)
    #     video_dir = os.path.join(comments_dir, video_id)
    #     step_size = 5 * 60
    #     search_slug = f"{search_string}_{step_size//60}m"
    #     figure_dir = os.path.join(comments_dir, "..", "searches", search_slug)

    #     try:
    #         os.mkdir(figure_dir)
    #     except Exception:
    #         pass

    #     figure_filename = os.path.join(figure_dir, f"{video_id}.png")
    #     save_plots_from_comment_comparisons_for_search_string_from_dir(
    #         video_id,
    #         search_string,
    #         figure_filename=figure_filename,
    #         overwrite=False,
    #         file_dir=video_dir,
    #         step_size=step_size
    #     )
