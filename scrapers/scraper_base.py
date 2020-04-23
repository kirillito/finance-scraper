import requests
from bs4 import BeautifulSoup


class ScraperBase(object):
    BASE_URL = None

    def _get_soup(self, url):
        html = requests.get(url).content
        return BeautifulSoup(html, 'lxml')

    def _convert_to_soup(self, html):
        return BeautifulSoup(str(html), 'lxml')

    def _get_url(self, ticker):
        return '{}?s={}'.format(self.BASE_URL, ticker)
