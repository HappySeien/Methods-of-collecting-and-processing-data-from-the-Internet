from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
import re


def get_data(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }

    response = requests.get(url=url, headers=headers)
    soup = bs(response.content, 'html.parser')
    return soup 


def get_page(data):
    page = data.find('li', class_='next').find('a')['href']
    return page


def parse_data(data):
    quote = data.find_all(attrs={'class': 'quote'})
    result = []

    for i in quote:
        data = {
            'quote': i.find('span', attrs={'class': 'text'}).get_text(strip=True),
            'author': i.find('small', attrs={'class': 'author'}).get_text(strip=True),
            'tags': [t.get_text(strip=True) for t in i.find_all('a', attrs={'class': 'tag'})],
        }
        result.append(data)
    return result


def main():
    page = ''
    result = []
    
    while True:
        URL = f'https://quotes.toscrape.com{page}'
        data = get_data(URL)
        try:
            page = get_page(data)
        except AttributeError as err:
            break
        result += parse_data(data)

    return result


if __name__ == '__main__':
    pprint(main())
