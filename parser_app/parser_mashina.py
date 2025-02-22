import requests
from bs4 import BeautifulSoup


URL = 'https://m.mashina.kg/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='list-item list-label')
    mashina_list = []
    for item in items:
        title = item.find('div', class_='block title').get_text(strip=True)
        price = item.find('div', class_='block price').get_text(strip=True)
        mashina_list.append({
            'title': title,
            'price': price,
        })
    return mashina_list


def mashina_parsing():
    response = get_html(URL)
    if response.status_code == 200:
        mashina_list_2 = []
        for page in range(1,2):
            response = get_html('https://m.mashina.kg/search/all/?region=all', params={'page': page})
            mashina_list_2.extend(get_data(response.text))
        return mashina_list_2
    else:
        raise Exception('Error in parsing mashina.kg')

