import mysql.connector
from flask import Flask , render_template, url_for, request, redirect
import database.create_accond as dbcreat
import database.login_user as dblog
import database.registration as dbreg
import database.conectDB as CDB


def serch_user(user):
    mydb = CDB.connect()
    mycursor = mydb.cursor()
    all_element = f"SELECT * FROM login WHERE EMAIL = '{user}'"
    mycursor.execute(all_element)

    for x in mycursor:
        id = x[0]
        email = x[1]
        password = x[2]
        name = x[3]

        return id,email,password,name

def login():
    CDB.connect_DB()
    if request.method == 'POST':
        mail = request.form['email']
        password = request.form['password']
        is_exist = dblog.serch_user(mail)
        login = 'login'
        if is_exist == None:
            return redirect(url_for('index_error', error=login))
        elif password != is_exist[2]:
            return redirect(url_for('index_error', error=login))
        else:
            db_name = is_exist[3]
            db_index = is_exist[0]
            return redirect(url_for('login', id=db_index))
