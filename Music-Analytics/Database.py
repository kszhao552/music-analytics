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
        cursor = db.cursor()
        
        return db
    except Error as e:
        raise(e)


def createDatabase(db, title):
    cursor = db.cursor()

    try:
        cursor.execute(f"create database IF NOT EXISTS {title}")
        print("Database created successfully")
    except Error as e:
        raise(e)
    
    CreateTracksQuery = """
    create TABLE IF NOT EXISTS Tracks (
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


    CreateArtistsQuery = """
    create TABLE IF NOT EXISTS Artists (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(70)
    )
    """

    CreateSongsQuery = """
    create TABLE IF NOT EXISTS Songs(
    FOREIGN KEY(track_id) REFERENCES track(id),
    FOREIGN KEY(artist_id) REFERENCES artist(id),
    PRIMARY KEY(track_id, artist_id)
    )
    """

    try:
        cursor.execute(CreateTracksQuery)
        cursor.execute(CreateArtistsQuery)
        cursor.execute(CreateSongsQuery)
        db.commit()
        print("Tables created successfully")
    except Error as e:
        raise(e)

def insertTable(track, db):
    if (track.id == ''):
        return 
    else:
        return


try:
    print(establishConnection())
except Error as e:
    print(f'Error: {e}')