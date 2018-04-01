import urllib3
from bs4 import BeautifulSoup

class SiteParser:
    @staticmethod
    def get_price(url):
        http = urllib3.PoolManager()
        page = http.request('GET', url)
        page = page.data.decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('span', attrs={'class': 'text-large2'})
        return name_box.text