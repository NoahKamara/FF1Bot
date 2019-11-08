import sqlite3
from datetime import date


def connect():
    connection = sqlite3.connect("f1sqlite.db")
    cursor = connection.cursor()
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='drivers' ''')

    # if the count is 1, then table exists
    if cursor.fetchone()[0] != 1:
        cursor.execute(
            '''CREATE TABLE "drivers" ("id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"name"	TEXT,"points" INTEGER, 
            "price" REAL, "date"	DATE) ''')

    return connection


def insertDrivers(drivers):
    datum = date.today().strftime("%Y-%m-%d")
    connection = connect()
    cursor = connection.cursor()
    for d in drivers:
        dataToInsert = (None, d.name, d.points, d.price, datum)
        cursor.execute("INSERT INTO 'drivers' VALUES (?, ?, ?, ?, ?);", dataToInsert)
    connection.commit()

    connection.close()
# never forget this, if you want the changes to be saved:
