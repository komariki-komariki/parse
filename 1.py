from bs4 import BeautifulSoup
import requests
from search_dict import HEADERS, KEYWORDS
from pprint import pprint
import re
articles_list = []


def text_article():
    HEADERS = {
        'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; habr_web_home=ARTICLES_LIST_ALL; hl=ru; fl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1-221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_wXDx2olu6kw',
        'Accept-Language': 'ru-RU,ru;q=0.9',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'sec-ch-ua-mobile': '?0'
    }
    url = 'https://habr.com/ru/all/'
    baseurl = 'https://habr.com/ru/'
    page = requests.get(url, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    tags = soup.findAll('a', class_='tm-article-snippet__hubs-item-link')
    name_news = soup.findAll('a', class_="tm-article-snippet__title-link")
    datetimes = soup.findAll('span', class_='tm-article-snippet__datetime-published')
    a = soup.find('div', class_='tm-articles-list')
    b = a.find_all('p')
    for text_article in name_news:
        print(text_article.text)
    for x in b:
        print(x.text)
    for tag in tags:
        print(tag.text)
    for links in soup.find_all('a', class_='tm-article-snippet__title-link'):
        print(baseurl + links.get('href'))
    for dates in datetimes:
        print(dates.text)



        #articles_list.append({'name': str(k) + '.jpg', 'tags': tag.text})
if __name__ == "__main__":
   text_article()