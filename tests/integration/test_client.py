from unittest import TestCase
from twitch_chat_log_analyzer.client import TwitchClient
from twitch_chat_log_analyzer.json_utils import load_json_file


class TestTwitchAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        data = load_json_file("creds.json")
        cls.client_id = data["client_id"]
        cls.client_secret = data["client_secret"]

    def test_initialize(self):
        """Test Initialization of TwitchClient"""
        _ = TwitchClient(self.client_id, self.client_secret)
