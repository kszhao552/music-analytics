from getpass import getpass
from mysql.connector import connect, Error
import Scraper
from Track import Track

#Track Table Schema:
#id
#title
#chart_year
#length
#tempo, dancability, energy, key, loudness, speechiness, acousticness, liveness, valence

#Artist Table Schema:
#id
#name

#Song Table Schema:
#track_id (Foreign key)
#artist_id (Foreign key)

def establishConnection():
    try:
        db = connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
        )
        print(db)
    except Error as e:
        print(e)

def createDatabase(db, title):
    cursor = db.cursor()

    cursor.execute(f"create database IF NOT EXISTS {title}")

establishConnection()