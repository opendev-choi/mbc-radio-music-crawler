import enum
from datetime import date
from urllib.parse import parse_qs

import requests
from bs4 import BeautifulSoup


MusicListIds = dict[str, str]


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
    ID_PER_PAGE = 10

    def __init__(self):
        pass

    def get_music_list(self, search_date: date = date.today(), program_code: ProgramCode = ProgramCode.MUSIC_CAMP):
        return self._search_music_list_code_by_date(search_date, program_code)

    def _search_music_list_ids_by_date(self, search_date: date, program_code: ProgramCode, page: int = 1) \
            -> MusicListIds:
        music_list_ids: MusicListIds = {}
        post_parameters = {
            'page': page,
            'progCode': program_code,
            'sdate': '',
            'edate': '',
            'searchType': SearchType.TITLE,
            'searchWord': '{d.year}년 {d.month}월 {d.day}일'.format(d=search_date)
        }
        response = requests.post(self.SEARCH_URL, data=post_parameters)

        parsed_response = BeautifulSoup(response.text, "html.parser")
        for td in parsed_response.find("div", {"id": "musicWrap"}).table.tbody.find_all('td'):
            if not td.a:
                continue
            *_, query_url = td.a['href'].split("?")
            music_list_ids[td.a.get_text()] = parse_qs(query_url)['seqID'][0]

        if self.ID_PER_PAGE == len(music_list_ids):
            return music_list_ids | self._search_music_list_ids_by_date(search_date, program_code, page + 1)
        else:
            return music_list_ids

    def _get_music_list(self):
        pass

    def _get_program_code_from_query(self, ):
        pass
