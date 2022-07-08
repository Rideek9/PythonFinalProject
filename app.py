"""This is a main file our app. In this file we have all route to all website
 All application is creat in Flask framework, and use MySQL Data Base"""

from flask import Flask , render_template, url_for, request
import database.create_accond as dbcreat
import database.login_user as dblog

app = Flask(__name__)



@app.route('/' , methods =['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def user():
    if request.method == 'POST':
        mail = request.form['email']
        password = request.form['password']
        is_exist = dblog.serch_user(mail)
        error_user = f"Użytkownik bądź hasło są nieprawidłowe"
        if is_exist == None:
            return render_template('index.html', error_user = error_user )
        elif password != is_exist[2]:
            return render_template('index.html', error_user=error_user)
        else:
            db_name = is_exist[3]
            db_index = is_exist[0]
            return render_template('user.html', name = db_name), db_index