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
    
    str = """
    create TABLE Tracks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(70), 
        year YEAR(4), 
        length DECIMAL(7, 3),
        dancebility DECIMAL(5, 3),
        energy DECIMAL(5, 3), 
        liveness DECIMAL(5, 3),
        loudness DECIMAL(6, 3),
        speechiness DECIMAL (5, 3),
        tempo DECIMAL (7, 3),
        valence DECIMAL(5, 3)
    )
    """

    cursor.execute(str)

    str = """
    create TABLE Artists (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(70)
    )
    """
    cursor.execute(str)

    str = """
    create TABLE Songs(
    FOREIGN KEY(track_id) REFERENCES track(id),
    FOREIGN KEY(artist_id) REFERENCES artist(id),
    PRIMARY KEY(track_id, artist_id)
    )
    """
    cursor.execute(str)

establishConnection()