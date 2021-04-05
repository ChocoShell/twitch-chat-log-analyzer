from unittest import TestCase
from twitch_chat_log_analyzer.api_v5 import TwitchAPIv5
from twitch_chat_log_analyzer.json_utils import load_json_file


class TestTwitchAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        data = load_json_file("creds.json")
        cls.client_id = data["client_id"]
        cls.api = TwitchAPIv5()

    def test_get_chat_for_video(self):
        video_id = "254274829"
        data = self.api.get_chat_for_video(self.client_id, video_id)
        self.assertIsNotNone(data)

    def test_get_clip(self):
        slug = "PeppyEndearingSeahorseDxCat"
        data = self.api.get_clip(self.client_id, slug)
        self.assertIsNotNone(data)
