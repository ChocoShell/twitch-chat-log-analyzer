"""Comes from: https://github.com/PetterKraabol/Twitch-Python/blob/master/twitch/v5/resources/comments.py"""
from typing import List, Optional, Dict, Any

from .base_model import BaseModel


class Commenter:
    def __init__(self, data: Dict[str, Any]):
        self.data: Dict[str, Any] = data

        self.display_name: str = data.get("display_name")
        self.id: str = data.get("_id")
        self.name: str = data.get("name")
        self.type: str = data.get("type")
        self.bio: str = data.get("bio")
        self.created_at: str = data.get("created_at")
        self.updated_at: str = data.get("updated_at")
        self.logo: str = data.get("logo")


class Emoticon:
    def __init__(self, data: Dict[str, Any]):
        self.data: Dict[str, Any] = data

        self.id: str = data.get("_id")
        self.begin: int = data.get("begin")
        self.end: int = data.get("end")
        self.emoticon_id: str = data.get("emoticon_id")
        self.emoticon_set_id: str = data.get("emoticon_set_id")


class Fragment:
    def __init__(self, data: Optional[Dict[str, Any]] = None):
        self.data: Dict[str, Any] = data

        self.text: str = data.get("text")
        self.emoticon: Optional[Emoticon] = (
            Emoticon(data.get("emoticon")) if data.get("emoticon") else None
        )


class UserBadge:
    def __init__(self, data: Dict[str, Any]):
        self.data: Dict[str, Any] = data

        self.id: str = data.get("_id")
        self.version: str = data.get("version")


class Message:
    def __init__(self, data: Dict[str, Any]):
        self.data: Dict[str, Any] = data

        self.body: str = data.get("body")
        self.emoticons: List[Emoticon] = [
            Emoticon(data) for data in data.get("emoticons", [])
        ]
        self.fragments: List[Fragment] = [
            Fragment(data) for data in data.get("fragments", [])
        ]
        self.is_action: bool = data.get("is_action")
        self.user_badges: List[UserBadge] = [
            UserBadge(data) for data in data.get("user_badges", [])
        ]
        self.user_color: str = data.get("user_color")


class Comment(BaseModel):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

        self.id: str = data.get("_id")
        self.created_at: str = data.get("created_at")
        self.updated_at: str = data.get("updated_at")
        self.channel_id: str = data.get("channel_id")
        self.content_type: str = data.get("content_type")
        self.content_id: str = data.get("content_id")
        self.content_offset_seconds: float = data.get("content_offset_seconds")
        self.commenter: Commenter = Commenter(data.get("commenter"))
        self.source: str = data.get("source")
        self.state: str = data.get("state")
        self.message: Message = Message(data.get("message"))
        self.more_replies: bool = data.get("more_replies")


class FilteredComment(BaseModel):
    def __init__(self, data: Dict[str, Any]):
        super().__init__(data)

        self.id: str = data.get("_id")
        self.created_at: str = data.get("created_at")
        self.updated_at: str = data.get("updated_at")
        self.channel_id: str = data.get("channel_id")
        self.content_type: str = data.get("content_type")
        self.content_id: str = data.get("content_id")
        self.content_offset_seconds: float = data.get("content_offset_seconds")
        self.commenter_display_name: str = data.get("commenter").get("display_name")
        self.commenter_id: str = data.get("commenter").get("_id")

        self.source: str = data.get("source")
        self.state: str = data.get("state")
        self.more_replies: bool = data.get("more_replies")
        self.body: Message = Message(data.get("message")).body

    def dict(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "channel_id": self.channel_id,
            "content_type": self.content_type,
            "content_id": self.content_id,
            "content_offset_seconds": self.content_offset_seconds,
            "commenter_display_name": self.commenter_display_name,
            "commenter_id": self.commenter_id,
            "source": self.source,
            "state": self.state,
            "more_replies": self.more_replies,
            "body": self.body,
        }
