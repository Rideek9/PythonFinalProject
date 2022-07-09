import mysql.connector
from flask import Flask , render_template, url_for, request, redirect
import database.create_accond as dbcreat
import database.login_user as dblog
import database.registration as dbreg
import database.conectDB as CDB
from googletrans import Translator



mydb = CDB.connect()

mycursor = mydb.cursor()


def user(id):
    all_element = f"SELECT * FROM login WHERE ID = '{id}'"
    mycursor.execute(all_element)

    for x in mycursor:
        id = x[0]
        email = x[1]
        password = x[2]
        name = x[3]

        return id, email, password, name


def translator(word,la1,la2):
    if word != "":
        trans = Translator()
        element = trans.translate(word,src=la1,dest=la2)
        return element.text
    else:
        return 'Podaj słowo'

