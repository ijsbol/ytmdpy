__all__ = (
    "Command",
    "RepeatMode",
)


from enum import StrEnum


class Command(StrEnum):
    PLAY_PAUSE = "playPause"
    PLAY = "play"
    PAUSE = "pause"
    VOLUME_UP = "volumeUp"
    VOLUME_DOWN = "volumeDown"
    SET_VOLUME = "setVolume"
    MUTE = "mute"
    UNMUTE = "unmute"
    SEEK_TO = "seekTo"
    CHANGE_VIDEO = "changeVideo"
    NEXT = "next"
    previous = "previous"
    REPEAT_MODE = "repeatMode"
    SHUFFLE = "shuffle"
    PLAY_QUEUE_INDEX = "playQueueIndex"
    TOGGLE_LIKE = "toggleLike"
    TOGGLE_DISLIKE = "toggleDislike"

class RepeatMode(StrEnum):
    NONE = "NONE"
    ALL = "ALL"
    ONE = "ONE"
