from datetime import date

SEARCH_URL = "http://miniweb.imbc.com/Music/Search"
PROGRAM_CODE = {'music_camp': 'RAMFM300'}


class MusicCamp:
    def __init__(self):
        pass

    def get_music_list(self, search_date: date = date.today()):
        pass

    def _search_music_list_code(self, search_date: date) -> int:
        pass

    def _get_music_list(self):
        pass
