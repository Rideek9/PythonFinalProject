import mysql.connector

mydb = mysql.connector.connect(
    host="sql46.lh.pl",
    user="serwer55600_projekpython",
    password="Python2022!",
    database="serwer55600_projekpython"

)

mycursor = mydb.cursor()

def serch_user(user):
    all_element = f"SELECT * FROM login WHERE EMAIL = '{user}'"
    mycursor.execute(all_element)

    for x in mycursor:
        id = x[0]
        email = x[1]
        password = x[2]
        name = x[3]

        return id,email,password,name


