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
        
        print("Connection to MySQL Server Successful")
        return db
    except Error as e:
        raise(e)

def restablishConnection(database):
    try:
        db = connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            db = database
        )
        cursor = db.cursor()
        
        print("Connection to MySQL Database Successful")
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


def createTables(db):
    
    CreateTracksQuery = """
    create TABLE IF NOT EXISTS Tracks (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        title VARCHAR(70), 
        chart_year YEAR(4),
        release_year YEAR(4),
        length DECIMAL(7, 3), 
        dancebility DECIMAL(5, 3), 
        energy DECIMAL(5, 3), 
        liveness DECIMAL(5, 3), 
        loudness DECIMAL(6, 3), 
        speechiness DECIMAL (5, 3), 
        tempo DECIMAL (7, 3), 
        music_key INT, 
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
    track_id INT NOT NULL,
    artist_id INT NOT NULL,
    PRIMARY KEY(track_id, artist_id),
    FOREIGN KEY(track_id) REFERENCES Tracks(id), 
    FOREIGN KEY(artist_id) REFERENCES Artists(id)
    )
    """

    try:
        cursor = db.cursor()
        cursor.execute(CreateTracksQuery)
        print("Tracks Table Created Successfully")
        cursor.execute(CreateArtistsQuery)
        print("Artists Table Created Successfully")
        cursor.execute(CreateSongsQuery)
        print("Songs Table Created Successfully")
        db.commit()
        print("Tables created successfully")
    except Error as e:
        raise(e)


def insertTable(track, db):
    if (track.id == ''):
        return 
    else:
        return



if __name__ == "__main__":
    try:
        db = restablishConnection("test")
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")
        results = cursor.fetchall()
        for result in results:
            print(result)
    except Error as e:
        print(f'Error: {e}')