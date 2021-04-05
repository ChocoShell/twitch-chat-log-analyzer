from unittest import TestCase
from twitch_chat_log_analyzer.clients.apis.api_v5 import TwitchAPIv5
from ...utils import load_creds


class TestTwitchAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client_id, _, _ = load_creds()
        cls.api = TwitchAPIv5()

    def test_get_chat_for_video(self):
        video_id = "254274829"
        data = self.api.get_chat_for_video(self.client_id, video_id)
        self.assertIsNotNone(data)

    def test_get_clip(self):
        slug = "PeppyEndearingSeahorseDxCat"
        data = self.api.get_clip(self.client_id, slug)
        self.assertIsNotNone(data)
