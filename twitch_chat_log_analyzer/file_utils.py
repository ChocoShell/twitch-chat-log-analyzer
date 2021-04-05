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
