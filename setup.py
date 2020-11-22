import sys
from setuptools import setup, find_packages

if sys.version_info < (3,9):
    sys.exit('Sorry, Python < 3.9 is not supported')

setup(name='mbcradiomusic',
      version='0.0.1',
      url='https://github.com/opendev-choi/mbc-radio-music-crawler',
      author='opendev.choi',
      author_email='opendev.choi@gmail.com',
      description='Crawl Music List From MBC Radio',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      install_requires=['cython', 'requests', 'beautifulsoup4'],
      zip_safe=False
)