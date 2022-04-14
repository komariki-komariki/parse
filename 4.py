from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re
from datetime import datetime
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

    # news = soup.find('div', class_='tm-articles-subpage').find('article', class_="tm-articles-list__item")
    # names = news.find('a', class_="tm-article-snippet__title-link").text
    # texts = news.find('div', class_="article-formatted-body article-formatted-body_version-2")
    # times = news.find('span', class_='tm-article-snippet__datetime-published').text.strip()
    # times2 = news.find('time')['datetime']
    # links = news.find('a', class_='tm-article-snippet__title-link')['href']
    test2 = soup.findAll('article', class_="tm-articles-list__item")
    # tags = news.findAll('a', class_='tm-article-snippet__hubs-item-link')


    for i in test2:
        tag_list = []
        name = i.find('a', class_="tm-article-snippet__title-link").text
        tags = i.findAll('a', class_='tm-article-snippet__hubs-item-link')
        for tag in tags:
            tag_list.append(tag.text.replace('*','').strip())
        try:
            texts = i.find('div', class_="article-formatted-body article-formatted-body_version-2").text.strip().replace('\n','').replace('\xa0','').replace('\r','')
        except:
            texts = i.find('div', class_="article-formatted-body article-formatted-body_version-1").text.strip().replace('\n','').replace('\xa0','').replace('\r','')
        dates = i.find('time')['datetime']
        links = baseurl + i.find('a', class_='tm-article-snippet__title-link')['href']
        articles_list.append([[name], [dates], tag_list, [texts], [links]])

    pprint(articles_list)

if __name__ == "__main__":
   text_article()