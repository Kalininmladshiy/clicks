import requests
import os


def shorten_link(token, url):
    url_bitly = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    body = {"long_url": url}
    response = requests.post(url_bitly, json=body, headers=headers)
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, bitlink):
    url_bitly = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(bitlink)
    headers = {'Authorization': 'Bearer {}'.format(token)}
    payload = {
        'units': -1,
        'unit': 'day',
    }
    response = requests.get(url_bitly, params=payload, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url):
    url_bitly = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(url_bitly, headers=headers)
    return response.ok

if __name__ == '__main__':
    token = os.environ.get('TOKEN')
    url = input('Введите ссылку, которую хотите сократить: ')
    if is_bitlink(url):
        print('Количество кликов: ', count_clicks(token, url))
    else:
        try:
            print('Битлинк', shorten_link(token, url))
            try:
                print('Количество кликов: ', count_clicks(token, shorten_link(token, url)))
            except requests.exceptions.HTTPError:
                print('неверные параметры запроса')
        except requests.exceptions.HTTPError:
            print('Вы неправильно ввели ссылку')
