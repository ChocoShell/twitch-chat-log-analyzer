from .json_utils import load_json_file
from .video_chapters import get_video_chapters


data = load_json_file("creds.json")
client_id = data["anon_client_id"]

video_id = "812219766"

video_chapters = get_video_chapters(client_id, video_id)

print(video_chapters)
