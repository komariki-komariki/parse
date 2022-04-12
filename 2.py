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
    a = soup.find('div', class_='tm-articles-list')

    #articles_list.append({id_article: {'article_name': pass, 'article_text': pass, 'article_date': pass, 'article_link': pass}})

    for id_article in soup.findAll('article', class_="tm-articles-list__item"):
        print(id_article['id'])
    for text_article in soup.findAll('a', class_="tm-article-snippet__title-link"):
        print(text_article.text)
    for x in a.findAll('p'):
        print(x.text)
    for tag in soup.findAll('a', class_='tm-article-snippet__hubs-item-link'):
        print(tag.text)
    for links in soup.findAll('a', class_='tm-article-snippet__title-link'):
        print(baseurl + links.get('href'))
    for dates in soup.findAll('span', class_='tm-article-snippet__datetime-published'):
        print(dates.text)

if __name__ == "__main__":
   text_article()