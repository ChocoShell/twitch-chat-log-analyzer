from unittest import TestCase
from twitch_chat_log_analyzer.client_v5 import TwitchClientv5
from twitch_chat_log_analyzer.json_utils import load_json_file


class TestTwitchAPIv5(TestCase):
    @classmethod
    def setUpClass(cls):
        data = load_json_file("creds.json")
        cls.client_id = data["client_id"]

    def test_initialize(self):
        """Test Initialization of TwitchClientv5"""
        _ = TwitchClientv5(self.client_id)
