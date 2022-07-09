from flask import Flask , render_template, url_for, request, redirect
import database.create_accond as dbcreat
import database.login_user as dblog

app = Flask(__name__)


@app.route('/' , methods =['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/error/<error>', methods = ['GET','POST'])
def index_error(error):
    user_error = f"login bądź hasło nieprawidłowe"
    if error == 'Login-false':
        return render_template('index.html', error_user = user_error)
    elif error == 'registration.html':
        return redirect('/registration.html')
    else:
        return render_template('error404.html')


@app.route('/login', methods = ['GET', 'POST'])
def user():
    if request.method == 'POST':
        mail = request.form['email']
        password = request.form['password']
        is_exist = dblog.serch_user(mail)
        login = 'Login-false'
        if is_exist == None:
            return redirect(url_for('index_error', error = login))
        elif password != is_exist[2]:
            return redirect(url_for('index_error', error = login))
        else:
            db_name = is_exist[3]
            db_index = is_exist[0]
            return render_template('user.html', name = db_name), db_index

@app.route('/registration.html', methods = ['GET','POST'])
def registration():
    return render_template('registration.html')