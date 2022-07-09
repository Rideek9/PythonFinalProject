import mysql.connector
import database.conectDB as CDB

mydb = CDB.connect()

def passwords():
    while True:
        password = input('Podaj hasło min 8 znaków\n--> ')
        if len(password)>=8 and not password.isupper() and not password.islower():
            return password
            break
        else:
            if not len(password)>=8:
                return "hasło za krótkie"
            elif password.isupper() or password.islower():
                return 'Muszą być małe i duże litery'

def user_name():
    name = input("Podaj swoje imię\n--> ")
    return name


def accound():
    mycursor = mydb.cursor()
    email_exists = "SELECT EMAIL, PASSWORD FROM login"
    mycursor.execute(email_exists)

    emails = []
    elements={}
    for x in mycursor:
        email = x[0]
        password = x[1]
        elements[email] = password
        emails.append(email)

    while True:
        email = input('Podaj email:\n--> ').lower()
        if email in emails:
            print('Mail istnieje')
            continue
        else:
            password = passwords()
            name = user_name()
            val=(email,password,name)
            add_element = "INSERT INTO login (EMAIL,PASSWORD,NAME) VALUES (%s,%s,%s)"
            mycursor.execute(add_element,val)
            mydb.commit()
            break


def main():
    accound()





