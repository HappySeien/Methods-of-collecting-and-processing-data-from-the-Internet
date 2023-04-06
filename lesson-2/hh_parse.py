import requests
from lxml import html
from pprint import pprint

#  translate(normalize-space(/tr/td/a), ' ', '')
# translate(/tr/td/a, ' &#9;&#10;&#13', '')

def hh_get_vacancy(vacancy, page=0):
    """
    """
    url = 'https://hh.ru/search/vacancy'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }
    params = {
        'text': vacancy,
        'area': '1',
        'page': page
    }

    response = requests.get(url=url, headers=headers, params=params)
    
    return response.text


def hh_parse_vacancy(data):
    """
    """
    dom = html.fromstring(data)
    # vacancy_list = dom.xpath('//div[@class="vacancy-serp-item-body__main-info"]')
    tittels = dom.xpath('//a[@class="serp-item__title"]/text()')
    company = dom.xpath('//a[@data-qa="vacancy-serp__vacancy-employer"]/text()')
    address = dom.xpath('//div[@data-qa="vacancy-serp__vacancy-address"]/text()')
    link = dom.xpath('//a[@class="serp-item__title"]/@href')
    result = []

    for i in range(len(link)):
        vacancy_data = {
            'tittle': tittels[i],
            'company': company[i],
            'address': address[i],
            'link': link[i],
            'site': 'hh.ru'
        }
        result.append(vacancy_data)
    return result



if __name__ == '__main__':
    data = hh_get_vacancy('python')
    result_list = hh_parse_vacancy(data)
    pprint(result_list)
    