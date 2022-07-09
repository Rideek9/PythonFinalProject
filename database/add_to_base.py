import mysql.connector
import database.conectDB as CDB
import googletrans

mydb = mysql.connector.connect(
    host="sql46.lh.pl",
    user="serwer55600_projekpython",
    password="Python2022!",
    database="serwer55600_projekpython"

)


mycursor = mydb.cursor()

def add_to_base(email):
    mydb = CDB.connect()
    mycursor = mydb.cursor()
    all_element = f"SELECT * FROM login WHERE EMAIL = '{email}'"
    mycursor.execute(all_element)

    for x in mycursor:
        id = x[0]
        email = x[1]
        password = x[2]
        name = x[3]
        fiszki = f"fiszki_user_{id}"
        mycursor.execute("CREATE TABLE %s (word VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_polish_ci, userLVL INT)" %(fiszki))




def add_word_to_tabel(id, words):
    mydb = CDB.connect()
    mycursor = mydb.cursor()
    el1 = words
    el2 = 1
    fiszki = f"fiszki_user_{id}"
    mycursor.execute("INSERT INTO %s VALUES('%s','%s')" % (fiszki,el1,el2))
    mydb.commit()


def all_element(id):
    mydb = CDB.connect()
    mycursor = mydb.cursor()
    fiszki = f"fiszki_user_{id}"
    mycursor.execute("SELECT DISTINCT word FROM %s ORDER BY word" % (fiszki))
    el = []
    for x in mycursor:
       el.append(x[0])

    return el





