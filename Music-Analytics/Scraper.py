import requests
from pprint import pprint
from Track import Track
from bs4 import BeautifulSoup
from Spotify import Spotify
from pprint import pprint
import pandas as pd

def updateTrack(spot, track, result):
    track.updateID(result['tracks']['items'][0]['id'])
    track.updateLength(result['tracks']['items'][0]['duration_ms']/1000)
    track.updateAudioFeatures(spot.getAudioFeatures(track.id))

def createTrack(spot, result, year):
    rank = result.find('div', class_ = "ye-chart-item__rank")
    title = result.find('div', class_ = "ye-chart-item__title")
    artist = result.find('div', class_ = "ye-chart-item__artist")

    track = Track(int(rank.text.strip()), title.text.strip(), artist.text.strip(), year)
    search = spot.getTrack(track.name, track.artist)
    
    try:
       updateTrack(spot, track, search)
    except Exception:
        search = spot.getTrackTitle(track.name)
        try:
            updateTrack(spot, track, search)
        except Exception:
            pass

    return track


def getLists(start, end):
    yearEndLists = []
    spot = Spotify()

    for i in range(start, end):

        URL = f'https://www.billboard.com/charts/year-end/{i}/hot-100-songs'
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find_all('article', class_ = "ye-chart-item")
   
        for result in results:
            
            track = createTrack(spot, result, i)
            pprint(track)
            yearEndLists.append(track)
            
    return yearEndLists

def dfToCsv(df, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        df.to_csv(f, header=f.tell()==0, index=False, line_terminator='\n')
    f.close()

if __name__ == "__main__":
    ls = getLists(2013, 2021)
    for item in ls:
        if item.id != '':
            dfToCsv(item.toDf(), 'output.csv')