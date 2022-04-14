from bs4 import BeautifulSoup
import requests
from pprint import pprint
import re
from search_dict import HEADERS, KEYWORDS, URL, BASEURL


articles_list = []

def text_article():
    page = requests.get(URL, headers=HEADERS).content
    soup = BeautifulSoup(page, "html.parser")
    test2 = soup.findAll('article', class_="tm-articles-list__item")
    for i in test2:
        tag_list = []
        name = i.find('a', class_="tm-article-snippet__title-link").text
        tags = i.findAll('a', class_='tm-article-snippet__hubs-item-link')
        for tag in tags:
            tag_list.append(tag.text.strip())
        try:
            texts = i.find('div', class_="article-formatted-body article-formatted-body_version-2").text.strip()
        except:
            texts = i.find('div', class_="article-formatted-body article-formatted-body_version-1").text.strip()
        dates = i.find('time')['datetime']
        links = BASEURL + i.find('a', class_='tm-article-snippet__title-link')['href']
        articles_list.append([name, dates, tag_list, texts, links])

def search_words():
    for search_string in KEYWORDS:
        for n in range(len(articles_list)):
            names = "".join(articles_list[n][0])
            tags = "".join(articles_list[n][2])
            texts = "".join(articles_list[n][3])
            if re.findall(f'{search_string}', names) or re.findall(f'{search_string}', tags) or re.findall(
                    f'{search_string}', texts):
                return f"{articles_list[n][1]}\n{articles_list[n][0]}\n{articles_list[n][-1]}\n"


if __name__ == "__main__":
    text_article()
    print(search_words())