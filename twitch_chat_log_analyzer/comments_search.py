import os

from .json_utils import load_json_file, write_json_file
from .file_utils import find


def write_results_for_channel(channel, search_string, case_sense=True):
    comments_dir = f"./data/{channel}/comments"
    video_ids = os.listdir(comments_dir)

    directory_format = (comments_dir + "{}/comments.json").format

    write_search_results_for_ids(
        video_ids, directory_format, search_string, case_insensitive=not case_sense
    )


def write_search_results_for_ids(
    chat_ids, directory_format, search_string, case_insensitive=False, overwrite=False
):
    for chat_id in chat_ids:
        filename = directory_format(chat_id)
        write_search_results_for_file(
            filename,
            search_string,
            overwrite=overwrite,
            case_insensitive=case_insensitive,
        )


def is_in_string(sub_string, super_string, case_insensitive=False):
    if case_insensitive:
        return sub_string.lower() in super_string.lower()
    else:
        return sub_string in super_string


# Search comments
def search_chat(comments, search_string, case_insensitive=False):
    results = []
    for comment in comments:
        if is_in_string(
            search_string, comment["message"]["body"], case_insensitive=case_insensitive
        ):
            results.append(comment)
    return results


def search_chat_from_file(filename, search_string, case_insensitive=False):
    comments = load_json_file(filename)
    return search_chat(comments, search_string, case_insensitive=case_insensitive)


def search_chat_dir(chat_dir, search_string):
    # Search chat_dir for .jsons
    chat_files = find("*.json", chat_dir)

    for filename in chat_files:
        search_chat_from_file(filename, search_string)


def write_search_results_for_file(
    comments_path, search_string, overwrite=False, case_insensitive=False
):
    comments_dir, comments_file = os.path.split(comments_path)
    search_string_file = os.path.join(comments_dir, f"{search_string}_{comments_file}")

    if os.path.isfile(search_string_file) and not overwrite:
        print(f"{search_string_file} exists")
        return

    if not os.path.isfile(comments_path):
        print(f"{comments_path} does not exist")
        return

    search_results = search_chat_from_file(
        comments_path, search_string, case_insensitive=case_insensitive
    )

    write_json_file(search_results, search_string_file)

    return search_string_file
