import enum
from dataclasses import dataclass


MusicListIds = dict[str, str]


@dataclass
class Music:
    title: str = 'Songs'
    singer: str = 'Various Artists'


class AutoValuedEnum(enum.Enum):
    def __str__(self):
        return str(self.value)


class ProgramCode(AutoValuedEnum):
    MUSIC_CAMP = 'RAMFM300'


class SearchType(AutoValuedEnum):
    TITLE = 1
    SINGER = 2
    SONG = 3
