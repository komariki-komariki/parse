from search_dict import KEYWORDS
from bs4 import BeautifulSoup
import requests
from pprint import pprint
def abc():
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
    filteredNews = []
    name_news_dict = []
    datetimes_dict =[]
    links_dict = []
    page = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(page, "html.parser")
    all_info = soup.findAll('article', class_="tm-articles-list__item")
    datetimes = soup.findAll('span',class_='tm-article-snippet__datetime-published')
    name_news = soup.findAll('a', class_="tm-article-snippet__title-link")
    tags = soup.findAll('a', class_='tm-article-snippet__hubs-item-link')
    # text_news = soup.findAll('div', class_="article-formatted-body article-formatted-body_version-1")
    for links in soup.find_all('a', class_='tm-article-snippet__title-link'):
        links_dict.append(baseurl+links.get('href'))
    #pprint(all_info)
    # allNews = soup.findAll('a', class_="tm-article-snippet__title-link")
    # pprint(allNews)
    #pprint(soup)



    for title in name_news:
        if title.find('span') is not None:
            name_news_dict.append(title.text)

    for tag in tags:
        if tag.find('span') is not None:
             filteredNews.append(tag.text)

    for dates in datetimes:
        if dates.find('time') is not None:
             datetimes_dict.append(dates.text)
    print(name_news_dict)
    print(filteredNews)
    print(datetimes_dict)
    print(links_dict)


if __name__ == "__main__":
   abc()
