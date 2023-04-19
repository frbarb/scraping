from bs4 import BeautifulSoup
import requests

def get_currency(in_curr, out_curr):
    url = f'https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])

    return rate

current_rate = get_currency('EUR', 'AUD')
print(current_rate)