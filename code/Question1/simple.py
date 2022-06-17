import requests
from bs4 import BeautifulSoup

BASE_URL = "[Lottery URL]?id={}"


def extract_draw_numbers(page_content):
    game_content = soup.find('div', id='page-content')
    h2_data = game_content.find_all('h2')
    game_data = h2_data[2]
    game_data = game_data.text \
        .replace('Winning Numbers: ', '|') \
        .replace('Powerball: ', '|') \
        .replace('Power Play: ', '|') \
        .split('|')
    game_data = [item.strip().replace(' ', ',') for item in game_data]
    return game_data

draw_data_list = []

for i in range(1, 72738):
    resp = requests.get(BASE_URL.format(72650))
    if 'Powerball' in resp.text: #TODO: Fix this so it actually works:
        soup = BeautifulSoup(resp.text, 'lxml')
        draw_data = extract_draw_numbers(soup)
        draw_data_list.append(draw_data)