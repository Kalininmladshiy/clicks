import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def shorten_link(token, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    body = {"long_url": url}
    response = requests.post(
        bitly_url,
        json=body,
        headers=headers,
    )
    response.raise_for_status()
    bitlink = response.json()['id']
    return bitlink


def count_clicks(token, bitlink):
    bitly_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    payload = {
        'units': -1,
        'unit': 'day',
    }
    response = requests.get(
        bitly_url,
        params=payload,
        headers=headers,
    )
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    headers = {'Authorization': 'Bearer {}'.format(token)}
    response = requests.get(
        bitly_url,
        headers=headers,
    )
    return response.ok


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser(
        description='Программа для сокращения ссылок в сервисе Bitly.'
    )
    parser.add_argument("url", help='Ссылка которую хоите сократить')
    args = parser.parse_args()
    url_parts = urlparse(args.url)
    url_to_check = f'{url_parts.netloc}{url_parts.path}'
    if is_bitlink(url_to_check):
        try:
            print('Количество кликов: ', count_clicks(token, url_to_check))
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
    else:
        try:
            print('Битлинк', shorten_link(token, args.url))
        except requests.exceptions.HTTPError:
            print('Вы неправильно ввели ссылку')
    