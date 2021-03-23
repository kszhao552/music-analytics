from getpass import getpass
from mysql.connector import connect, Error
import Scraper
from Track import Track

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


establishConnection()