from datetime import date
from urllib.parse import parse_qs

import requests
from bs4 import BeautifulSoup

from constants import MusicListIds, SearchType, Music, ProgramCode, NoSearchResultException


class MusicCamp:
    SEARCH_URL = "http://miniweb.imbc.com/Music/Search"
    LIST_URL = "http://miniweb.imbc.com/Music/View"
    ID_PER_PAGE = 10

    def get_music_list_by_date(self, search_date: date = date.today(),
                               program_code: ProgramCode = ProgramCode.MUSIC_CAMP) -> list[Music]:
        music_list: list[Music] = []
        music_list_ids = self._search_music_list_ids_by_date(search_date, program_code)
        if len(music_list_ids) == 0:
            raise NoSearchResultException("No Search result at '{d.year}년 {d.month}월 {d.day}일'".format(d=search_date))

        for title, music_list_id in music_list_ids.items():
            music_list += self._get_music_list_by_id(music_list_id, program_code)

        return music_list

    def _search_music_list_ids_by_date(self, search_date: date, program_code: ProgramCode, page: int = 1) \
            -> MusicListIds:
        post_parameters = {
            'page': page,
            'progCode': program_code,
            'sdate': '',
            'edate': '',
            'searchType': SearchType.TITLE,
            'searchWord': '{d.year}년 {d.month}월 {d.day}일'.format(d=search_date)
        }
        response = requests.post(self.SEARCH_URL, data=post_parameters)
        music_list_ids: MusicListIds = self._parse_music_id_list_from_page(response.text)

        if self.ID_PER_PAGE == len(music_list_ids):
            return music_list_ids | self._search_music_list_ids_by_date(search_date, program_code, page + 1)
        else:
            return music_list_ids

    def _get_music_list_by_id(self, music_list_id: str, program_code: ProgramCode) -> list[Music]:
        get_parameters = {
            'progCode': program_code,
            'seqID': music_list_id
        }
        response = requests.get(self.LIST_URL, params=get_parameters)
        music_list: list[Music] = self._parse_music_list_from_page(response.text)

        return music_list

    def _parse_music_id_list_from_page(self, html: str) -> MusicListIds:
        music_list_ids: MusicListIds = {}

        parsed_response = BeautifulSoup(html, "html.parser")
        for td in parsed_response.find("div", {"id": "musicWrap"}).table.tbody.find_all('td'):
            if not td.a:
                continue
            *_, query_url = td.a['href'].split("?")
            music_list_ids[td.a.get_text()] = parse_qs(query_url)['seqID'][0]

        return music_list_ids

    def _parse_music_list_from_page(self, html: str) -> list[Music]:
        music_list: list[Music] = []
        parsed_response = BeautifulSoup(html, "html.parser")

        for tr in parsed_response.table.find_all('tr'):
            music = Music()
            for td in tr.find_all('td'):
                if td.p:
                    if td.p['class'][0] == 'title':
                        music.title = td.p.text
                    elif td.p['class'][0] == 'singer':
                        music.singer = td.p.text

                        music_list.append(music)
                        music = Music()

        return music_list
