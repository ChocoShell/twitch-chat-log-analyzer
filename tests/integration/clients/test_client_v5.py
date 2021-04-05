from unittest import TestCase
from twitch_chat_log_analyzer.clients.client_v5 import TwitchClientv5
from ..utils import load_creds


class TestTwitchAPIv5(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client_id, _, _ = load_creds()

    def test_initialize(self):
        """Test Initialization of TwitchClientv5"""
        _ = TwitchClientv5(self.client_id)
