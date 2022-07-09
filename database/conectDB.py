import mysql.connector


def connect():
    mydb = mysql.connector.connect(
        host="sql46.lh.pl",
        user="serwer55600_projekpython",
        password="Python2022!",
        database="serwer55600_projekpython"

    )
    return mydb

def connect_DB():
    mydb = mysql.connector.connect(
        host="sql46.lh.pl",
        user="serwer55600_projekpython",
        password="Python2022!",
        database="serwer55600_projekpython"

    )
    con = mydb.cursor()
    return con

