from twitch_chat_log_analyzer.json_utils import load_json_file


creds_file = "creds.json"


def load_creds(filename=creds_file):
    data = load_json_file(filename)
    client_id = data["client_id"]
    client_secret = data["client_secret"]
    anon_client_id = data["anon_client_id"]

    return client_id, client_secret, anon_client_id
