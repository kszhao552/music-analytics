import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import Track
from bs4 import BeautifulSoup

def getLists():
    yearEndLists = []

    for i in range(2006, 2021):

        URL = f'https://www.billboard.com/charts/year-end/{i}/hot-100-songs'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find_all('article', class_ = "ye-chart-item")
   
        for result in results:
            
        
            yearEndLists.append(Track(int(rank.text.split('\n')[1]), title.text.split('\n')[1], artist.text.split('\n')[int(len(artist.text.split('\n'))/2)], i))

        return yearEndLists







