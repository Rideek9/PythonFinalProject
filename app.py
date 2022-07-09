from flask import Flask , render_template, url_for, request, redirect
import database.create_accond as dbcreat
import database.login_user as dblog
import database.registration as dbreg
import database.conectDB as CDB
import database.translator as Trans

app = Flask(__name__)


@app.route('/' , methods =['GET', 'POST'])
def index():
        return render_template('index.html')


@app.route('/error/<error>', methods = ['GET','POST'])
def index_error(error):
    CDB.connect_DB()
    user_error = f"login bądź hasło nieprawidłowe"
    add_user = f"Konto zostało stworzone. Gratulacje"
    if error == 'login':
        return render_template('index.html', error_user = user_error)
    elif error == 'registration':
        return redirect('/registration')
    elif error =='account_created':
        return render_template('index.html', correct = add_user)
    else:
        return render_template('error404.html')

@app.route('/user/id<id>', methods = ['GET','POST'])
def login(id):
    id_user = id
    elements = Trans.user(id)
    name = elements[3]
    return render_template('user.html', name = name)


@app.route('/login', methods = ['GET', 'POST'])
def user():
   return  dblog.login()

@app.route('/registration', methods = ['GET','POST'])
def registration():
    if request.method == 'POST':
        passwordOne = request.form['password']
        passswordSecond = request.form['passwordSecond']
        email = request.form['email']
        name = request.form['user_name']
        return dbreg.user_registration(passwordOne,passswordSecond,email,name)
    return render_template('registration.html')



