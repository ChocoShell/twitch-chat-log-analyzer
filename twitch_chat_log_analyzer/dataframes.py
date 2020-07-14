import pandas as pd
import os

from .models.comments import FilteredComment
from .json_utils import load_json_file

# Pandas, FileIO, os searches


def comment_data_to_df(comments):
    flattened_comments = [FilteredComment(comment).dict() for comment in comments]
    return pd.DataFrame(flattened_comments)


def comment_data_to_csv(comments, csv_filename):
    df = comment_data_to_df(comments)
    df.to_csv(csv_filename, index=False)


def comment_json_to_csv(comment_filename):
    comments = load_json_file(comment_filename)
    path, filename = os.path.split(comment_filename)
    name = filename.split(".")[0]

    csv_filename = f"{name}.csv"

    csv_filename = os.path.join(path, csv_filename)

    comment_data_to_csv(comments, csv_filename)


def convert_channel_comments_to_csv(channel):
    comments_dir = f"./data/{channel}/comments"
    video_ids = os.listdir(comments_dir)

    for video_id in video_ids:
        comment_json_path = os.path.join(comments_dir, video_id, "comments.json")
        if os.path.isfile(comment_json_path):
            comment_json_to_csv(comment_json_path)
        else:
            print(f"File not found for video id: {video_id}")
