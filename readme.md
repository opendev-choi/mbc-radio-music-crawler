## MBCMusicCrawler

> * MBC의 동의 없는 선곡 콘텐츠의 상업적 이용을 금합니다.

해당 코드 또한 MBC 의 요청대로 상업적으로 사용할수 없습니다 

해당 코드로 가져온 모든 선곡표의 저작권은 MBC 에 있음을 알립니다


### BASIC EXAMPLES
```python
import datetime
from mbcmusiccrawler.MBCMusicCrawler import MBCMusicCrawler

mbc_music_crawler = MBCMusicCrawler()

# specify Date
music_list = mbc_music_crawler.get_music_list_by_date(datetime.date.fromisoformat('2020-11-21'))

# non-specify Date (today)
music_list = mbc_music_crawler.get_music_list_by_date()


print(music_list)
```

### DETAIL
```python
def get_music_list_by_date(self, search_date: date = date.today(),
                               program_code: ProgramCode = ProgramCode.MUSIC_CAMP) -> list[Music]:
"""
get_music_list_by_date

:param search_date: datetime.date, search date
:param program_code: ProgramCode, search radio program code
:return: 
"""
    pass
```