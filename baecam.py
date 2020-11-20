import enum
from datetime import date

import requests


class AutoValuedEnum(enum.Enum):
    def __str__(self):
        return str(self.value)


class ProgramCode(AutoValuedEnum):
    MUSIC_CAMP = 'RAMFM300'


class SearchType(AutoValuedEnum):
    TITLE = 1
    SINGER = 2
    SONG = 3


class MusicCamp:
    SEARCH_URL = "http://miniweb.imbc.com/Music/Search"
    PROGRAM_CODE = {'music_camp': 'RAMFM300'}

    def __init__(self):
        pass

    def get_music_list(self, search_date: date = date.today()):
        pass

    def _search_music_list_code(self, search_date: date) -> int:
        pass

    def _get_music_list(self):
        pass
