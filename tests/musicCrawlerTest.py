from datetime import date
from unittest import TestCase
from unittest.mock import patch, PropertyMock

from mbcmusiccrawler.MBCMusicCrawler import MBCMusicCrawler, ProgramCode
from tests.constants import ONE_MUSIC_LIST_ID_HTML, ONE_PAGE_MUSIC_LIST_ID_HTML, MANY_PAGE_MUSIC_LIST_ID_HTML


class MusicCrawlerTest(TestCase):
    def setUp(self) -> None:
        self.music_crawler = MBCMusicCrawler()

    @patch('requests.post', return_value=PropertyMock(text=ONE_MUSIC_LIST_ID_HTML))
    def test_search_one_music_list_ids(self, mocked_requests):
        result = self.music_crawler._search_music_list_ids_by_date(date.today(), ProgramCode.MUSIC_CAMP)

        self.assertEqual(len(result), 1)
        self.assertEqual(mocked_requests.call_count, 1)

    def test_parse_music_id_list_from_page(self):
        pass

    def test_parse_music_list_from_page(self):
        pass
