from .models.video_chapters import VideoGQLChapters, ChapterNode
from .apis.gql_query import TwitchGQLQuery


def get_video_chapters(client_id, video_id):
    twitch_query_maker = TwitchGQLQuery(client_id)

    response = twitch_query_maker.get_chapters_from_video_id(video_id)

    return create_video_chapters_from_dict(response.json()[0])


def create_video_chapters_from_dict(video_dict):
    video_id = video_dict["data"]["video"]["id"]
    nodes = video_dict["data"]["video"]["moments"]["edges"]

    chapters = [create_chapter_node_from_dict(node) for node in nodes]

    chapters.sort(key=lambda x: x.position_milliseconds)

    return VideoGQLChapters(video_id, chapters)


def create_chapter_node_from_dict(node):
    node_dict = node["node"]
    node_id = node_dict["id"]
    position_milliseconds = node_dict["positionMilliseconds"]
    duration_milliseconds = node_dict["durationMilliseconds"]
    try:
        display_name = node_dict["details"]["game"]["displayName"]
    except Exception:
        display_name = node_dict["description"]

    return ChapterNode(
        node_id, position_milliseconds, duration_milliseconds, display_name
    )
