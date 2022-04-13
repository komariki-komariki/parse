from bs4 import BeautifulSoup
import requests
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

    a = soup.find('div', class_='tm-articles-subpage').find('article', class_="tm-articles-list__item").findAll('a', class_='tm-article-snippet__hubs-item-link')
    names = soup.find('div', class_='tm-articles-subpage').find('article', class_="tm-articles-list__item").findAll('a', class_="tm-article-snippet__title-link")
    texts = soup.find('div', class_='tm-articles-subpage').find('article', class_="tm-articles-list__item").findAll('div', class_="article-formatted-body article-formatted-body_version-2")
    test = soup.find('span', class_='tm-article-snippet__datetime-published').text.strip()
    print(test)
    test2 = soup.findAll('article', class_="tm-articles-list__item")
    print(len(test2))
    #for texts in test2:

    # for y in names:
    #     print(y.text)
    # for z in texts:
    #     print(z.text)
    # for x in a:
    #     articles_list.append(x.text)
    # print(articles_list)


if __name__ == "__main__":
   text_article()