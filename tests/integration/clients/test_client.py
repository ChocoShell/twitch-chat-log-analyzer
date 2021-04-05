from unittest import TestCase
from twitch_chat_log_analyzer.clients.client import TwitchClient
from ..utils import load_creds


class TestTwitchAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client_id, cls.client_secret, _ = load_creds()

    def test_initialize(self):
        """Test Initialization of TwitchClient"""
        _ = TwitchClient(self.client_id, self.client_secret)
