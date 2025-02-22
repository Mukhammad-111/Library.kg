import requests
from bs4 import BeautifulSoup


URL = 'https://bookhouse.kg/ru/'

HEADERS = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS ,params=params)
    return request


def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='book-inner uk-card uk-card-default uk-card-hover book_inner_padding uk-margin')
    book_house_list = []
    for item in items:
        image = item.find('div', class_='uk-width-1-1 uk-text-center uk-inline').find('img')['src']
        title = item.find('div', class_='uk-width-1-1 uk-padding-top-10').get_text(strip=True)
        author = item.find('div', class_='uk-text-muted mavish').get_text(strip=True)
        price = item.find('div', class_='uk-margin-small-top uk-text-bold').get_text(strip=True)
        book_house_list.append({
            'image':image,
            'title':title,
            'author':author,
            'price':price,
        })
    return book_house_list


def parsing_book_house():
    response = get_html(URL)
    if response.status_code == 200:
        book_house_list_2 = []
        for page in range(1,2):
            response = get_html('https://bookhouse.kg/ru/ebook/', params={'page':page})
            book_house_list_2.extend(get_data(response.text))
        return book_house_list_2
    else:
        raise Exception('Error in parsing book house')



