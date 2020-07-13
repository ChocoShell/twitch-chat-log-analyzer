import json


# JSON helpers
def write_json_file(data, filename):
    with open(filename, "w+") as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)


def load_json_file(filename):
    with open(filename) as json_file:
        return json.load(json_file)
