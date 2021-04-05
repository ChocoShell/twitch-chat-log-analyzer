from .json_utils import load_json_file
from .video_chapters import get_video_chapters
from .apis.api import TwitchAPI


data = load_json_file("creds.json")
anon_client_id = data["anon_client_id"]
client_id = data["client_id"]
client_secret = data["client_secret"]


def get_video_with_game_played_from_channel(
    client_id, client_secret, anon_client_id, channel_name, game_name
):
    token = TwitchAPI.get_twitch_oauth_token(client_id, client_secret)
    client = TwitchAPI()
    client.headers = {
        "Authorization": f"Bearer {token}",
        "Client-ID": client_id,
    }
    query_results = client.search_channels(channel_name)
    channel_id = query_results["data"][0]["id"]

    response = client.get_games(name=game_name)
    game_id = response["data"][0]["id"]

    video_data = client.get_videos(user_id=channel_id, first=100)
    # def get_all_videos(client, channel_id):

    print(len(video_data["data"]))
    video_ids = [item["id"] for item in video_data["data"]]

    video_by_chapters = [
        get_video_chapters(anon_client_id, video_id)
        for video_id in video_ids
    ]
    videos_with_game_played = []
    for video in video_by_chapters:
        for chapter in video.chapters:
            if chapter.game_id == game_id:
                videos_with_game_played.append(video)
                break

    return videos_with_game_played


# video_id = "812219766"

# video_chapters = get_video_chapters(anon_client_id, video_id)

# print(video_chapters)


# Among Us Streamers
"""
trainwreckstv
hasanabi
xqcow
"""

channel_name = "xqcow"
game_name = "Among Us"

response = get_video_with_game_played_from_channel(
    client_id, client_secret, anon_client_id, channel_name, game_name
)

print(response)
