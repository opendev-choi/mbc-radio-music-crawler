from datetime import date
from unittest import TestCase
from unittest.mock import patch, PropertyMock

from mbcmusiccrawler.MBCMusicCrawler import MBCMusicCrawler, ProgramCode
from tests.constants import ONE_MUSIC_LIST_ID_HTML, ONE_PAGE_MUSIC_LIST_ID_HTML, \
    MANY_PAGE_MUSIC_LIST_ID_HTML, MUSIC_LIST_HTML, TWO_MUSIC_LIST_ID_HTML


class MusicCrawlerTest(TestCase):
    def setUp(self) -> None:
        self.music_crawler = MBCMusicCrawler()

    @patch('requests.post', return_value=PropertyMock(text=ONE_MUSIC_LIST_ID_HTML))
    def test_search_one_music_list_ids(self, mocked_requests):
        result = self.music_crawler._search_music_list_ids_by_date(date.today(), ProgramCode.MUSIC_CAMP)

        self.assertEqual(len(result), 1)
        self.assertEqual(mocked_requests.call_count, 1)

    @patch('requests.post', side_effect=[PropertyMock(text=html) for html in ONE_PAGE_MUSIC_LIST_ID_HTML])
    def test_search_one_page_music_list_ids(self, mocked_requests):
        result = self.music_crawler._search_music_list_ids_by_date(date.today(), ProgramCode.MUSIC_CAMP)

        self.assertEqual(len(result), 10)
        self.assertEqual(mocked_requests.call_count, 2)

    @patch('requests.post', side_effect=[PropertyMock(text=html) for html in MANY_PAGE_MUSIC_LIST_ID_HTML])
    def test_search_many_page_music_list_ids(self, mocked_requests):
        result = self.music_crawler._search_music_list_ids_by_date(date.today(), ProgramCode.MUSIC_CAMP)

        self.assertEqual(len(result), 28)
        self.assertEqual(mocked_requests.call_count, 3)

    def test_parse_music_id_list_from_page(self):
        result = self.music_crawler._parse_music_id_list_from_page(TWO_MUSIC_LIST_ID_HTML)

        self.assertEqual(result['2020년 11월 24일 선곡표'], '1')
        self.assertEqual(result['2020년 11월 23일 선곡표'], '2')
        self.assertEqual(len(result), 2)

    def test_parse_music_list_from_page(self):
        result = self.music_crawler._parse_music_list_from_page(MUSIC_LIST_HTML)
        self.assertEqual(len(result), 2)

        # Gypsy King
        self.assertEqual(result[0].title, 'Volare')
        self.assertEqual(result[0].singer, 'Gypsy King')

        # The Jackson 5
        self.assertEqual(result[1].title, 'I Want You Back')
        self.assertEqual(result[1].singer, 'The Jackson 5')