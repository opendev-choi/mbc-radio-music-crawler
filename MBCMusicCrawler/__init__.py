import os
import sys

from mbcmusiccrawler import MBCMusicCrawler

real_path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
sys.path.append(real_path)

__all__ = ['MBCMusicCrawler']