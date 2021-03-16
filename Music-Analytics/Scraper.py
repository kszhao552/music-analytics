import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from bs4 import BeautifulSoup

for i in range(2006, 2021):

    URL = f'https://www.billboard.com/charts/year-end/{i}/hot-100-songs'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('article', class_ = "ye-chart-item")
   

    for result in results:
        rank = result.find('div', class_ = "ye-chart-item__rank")
        title = result.find('div', class_ = "ye-chart-item__title")
        artist = result.find('div', class_ = "ye-chart-item__artist")

        print(f'{rank.text.strip()} {title.text.strip()} - {artist.text.strip()}')





