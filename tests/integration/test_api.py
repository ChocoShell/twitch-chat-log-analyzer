from unittest import TestCase
from twitch_chat_log_analyzer.api import TwitchAPI
from twitch_chat_log_analyzer.json_utils import load_json_file


class TestTwitchAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        data = load_json_file("creds.json")
        client_id = data["client_id"]
        client_secret = data["client_secret"]
        token = TwitchAPI.get_twitch_oauth_token(client_id, client_secret)
        cls.api = TwitchAPI()
        cls.api.headers = {
            "Authorization": f"Bearer {token}",
            "Client-ID": client_id,
        }

    def test_search_channels(self):
        query = "lirik"
        data = self.api.search_channels(query)
        self.assertIsNotNone(data)

    def test_get_videos(self):
        user_id = "207813352"
        data = self.api.get_videos(user_id=user_id)
        self.assertIsNotNone(data)

    def test_get_clips(self):
        broadcaster_id = "207813352"
        data = self.api.get_clips(broadcaster_id=broadcaster_id)
        self.assertIsNotNone(data)

    def test_get_clips_optional_parameters(self):
        broadcaster_id = "207813352"
        data = self.api.get_clips(broadcaster_id=broadcaster_id, first=5)
        self.assertIsNotNone(data)