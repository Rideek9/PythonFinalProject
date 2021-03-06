import mysql.connector
from flask import Flask , render_template, url_for, request, redirect
import database.conectDB as CDB
import database.add_to_base as ADT


mydb = CDB.connect()

mycursor = mydb.cursor()


def creat_user(email,password,name):
    val = (email,password,name)
    add = "INSERT INTO login (EMAIL,PASSWORD,NAME) VALUES (%s,%s,%s)"
    mycursor.execute(add,val)
    mydb.commit()


def user_registration(passwordOne,passswordSecond,email,name):
        if passwordOne != passswordSecond:
            return render_template('registration.html' , error = 'Hasła nie są takie same' )
        elif len(passwordOne)<8:
            return render_template('registration.html', error='Hasła jest za krótkie')
        elif email =="":
            return render_template('registration.html', error='podaj email')
        elif name =="":
            return render_template('registration.html', error='Podaj imię')
        else:
            creat_user(email,passwordOne,name)
            ADT.add_to_base(email)
            return redirect(url_for('index_error', error= "account_created"))
