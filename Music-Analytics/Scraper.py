import requests
import spotipy
import pprint
from bs4 import BeautifulSoup

for i in range(2006, 2021):

    URL = f'https://www.billboard.com/charts/year-end/{i}/hot-100-songs'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('div', class_ = "ye-chart-item__title")
    artists = soup.find_all('div', class_ = "ye-chart-item__artist")

    for result in results:
        print(result.text.strip())

    print()

    for artist in artists:
        print(artist.text.strip())

