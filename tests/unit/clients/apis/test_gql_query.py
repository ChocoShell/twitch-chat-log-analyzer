from unittest import TestCase
import json

from twitch_chat_log_analyzer.clients.apis.gql_query import TwitchGQLQuery


class TestTwitchGQLQuery(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = TwitchGQLQuery("fake_client_id")

    def test_generate_video_chapters_for_video_id(self):
        video_id = "975294393"
        data = self.api.generate_video_chapters_for_video_id(video_id)
        data = json.loads(data)
        self.assertEqual(data[0].get("variables").get("videoID"), video_id)