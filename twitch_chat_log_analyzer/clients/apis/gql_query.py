import requests
import json


class TwitchGQLQuery:
    def __init__(self, client_id):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "Accept": "*/*",
            "Accept-Language": "en-US",
            "Client-Id": client_id,
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://www.twitch.tv",
            "Connection": "keep-alive",
        }
        # hard coded values that may change
        self.version = 1
        # Prolly tied to the auth token
        self.sha256_hash = (
            "b63c615e4fec1fbc3e6dd2d471c818886c4cf528c0cf99c136ba3981024f5e98"
        )

        self.url = "https://gql.twitch.tv/gql#origin=twilight"

    def generate_video_chapters_for_video_id(self, video_id):
        query = [
            {
                "operationName": "VideoPlayer_ChapterSelectButtonVideo",
                "variables": {"videoID": str(video_id)},
                "extensions": {
                    "persistedQuery": {
                        "version": self.version,
                        "sha256Hash": self.sha256_hash,
                    }
                },
            }
        ]
        return json.dumps(query)

    def get_chapters_from_video_id(self, video_id):
        body = self.generate_video_chapters_for_video_id(video_id)
        return requests.post(self.url, headers=self.headers, data=body)
