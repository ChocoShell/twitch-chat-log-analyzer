from unittest import TestCase
from twitch_chat_log_analyzer.clients.apis.gql_query import TwitchGQLQuery
from ...utils import load_creds


class TestTwitchGQLQuery(TestCase):
    @classmethod
    def setUpClass(cls):
        _, _, client_id = load_creds()
        cls.api = TwitchGQLQuery(client_id)

    def test_get_chapters_from_video_id(self):
        video_id = "975294393"
        data = self.api.get_chapters_from_video_id(video_id)
        self.assertGreater(len(data.json()), 0)
