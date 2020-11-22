from setuptools import setup, find_packages

setup(name='MBCMusicCrawler',
      version='0.0.1',
      url='https://github.com/opendev-choi/mbc-radio-music-crawler',
      author='opendev.choi',
      author_email='opendev.choi@gmail.com',
      description='Crawl Music List From MBC Radio',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=['cython'],
      zip_safe=False
)