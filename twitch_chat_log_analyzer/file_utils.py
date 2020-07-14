import os
import fnmatch


# Find Files
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def create_dir(dir_name, path):
    new_dir = os.path.join(path, dir_name)
    os.mkdir(new_dir)


def format_folder_structure(video_ids, comments_dir):
    dir_name = "partial"
    for video_id in video_ids:
        video_path = os.path.join(comments_dir, video_id)
        try:
            create_dir(dir_name, video_path)
        except FileExistsError:
            pass
        filtered_paths = filter(
            lambda path: dir_name not in path,
            find("comments_*.json", video_path),
        )
        for path in filtered_paths:
            cur_dir, filename = os.path.split(path)
            new_path = os.path.join(cur_dir, dir_name, filename)
            os.rename(path, new_path)


def rename_all_matching_files(pattern, search_dir, new_name):
    files = find(pattern, search_dir)
    for file in files:
        path, filename = os.path.split(file)
        new_path = os.path.join(path, new_name)
        os.rename(file, new_path)
