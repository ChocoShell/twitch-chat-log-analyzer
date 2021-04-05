from dataclasses import dataclass


@dataclass
class ChapterNode:
    node_id: str
    position_milliseconds: int
    duration_milliseconds: int
    display_name: str


class VideoGQLChapters:
    def __init__(self, video_id, chapters):
        self.video_id = video_id
        self.chapters = chapters

    def __repr__(self):
        return f"VideoGQLChapters: {self.video_id} - [{self.chapters}]"
