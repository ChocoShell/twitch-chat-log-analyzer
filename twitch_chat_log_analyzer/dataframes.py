import pandas as pd
import os

from .models.comments import FilteredComment
from .json_utils import load_json_file

# Pandas, FileIO, os searches


def convert_channel_comments_to_csv(channel, filename):
    comments_dir = f"./data/{channel}/comments"
    video_ids = os.listdir(comments_dir)

    for video_id in video_ids:
        comment_json_path = os.path.join(comments_dir, video_id, filename)
        if os.path.isfile(comment_json_path):
            convert_comment_json_to_csv(comment_json_path)
        else:
            print(f"File not found for video id: {video_id}")


def sort_dict(x, descending=False):
    return {
        k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=descending)
    }


def get_comment_df_from_channel_video_id(channel, video_id):
    csv_filename = f"./data/{channel}/comments/{video_id}/comments.csv"
    return pd.read_csv(csv_filename)


def convert_comments_to_df(comments):
    flattened_comments = [FilteredComment(comment).dict() for comment in comments]
    return pd.DataFrame(flattened_comments)


def convert_comments_to_csv(comments, csv_filename):
    df = convert_comments_to_df(comments)
    df.to_csv(csv_filename, index=False)


def convert_comment_json_to_csv(comment_filename):
    comments = load_json_file(comment_filename)
    path, filename = os.path.split(comment_filename)
    name = filename.split(".")[0]

    csv_filename = f"{name}.csv"

    csv_filename = os.path.join(path, csv_filename)

    convert_comments_to_csv(comments, csv_filename)
    return csv_filename
