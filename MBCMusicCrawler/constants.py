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
    DREAM_RADIO = 'FM4U000001200'
    B_SIDE = 'FM4U000001323'
    JUST_POP = 'FM4U000001304'
    MOVIE_MUSIC = 'FM4U000001296'
    KPOP_2000 = 'FM4U000001320'
    WORLD_OPEN_MORNING = 'FM4U000001000'
    GOODMORNING_FM = 'RAMFM240'
    TODAY_MORNING = 'FM4U000001070'
    GOLDEN_DISC = 'RAMFM260'
    TWO_HOUR_DATE = 'RAMFM280'
    AFTERNOON_DISCOVERY = 'FM4U000001258'


class SearchType(AutoValuedEnum):
    TITLE = 1
    SINGER = 2
    SONG = 3


class NoSearchResultException(Exception):
    pass
