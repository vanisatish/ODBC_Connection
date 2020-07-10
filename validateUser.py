import mysql.connector

mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='mysql4me', database='testdb')
print(mydb)

# creating a DB with a cursor. Cursor is an object that communicates with the entire mysql server
mycursor = mydb.cursor()

name = input('Enter Username: ')
checkUser = mycursor.execute('SELECT * FROM employee WHERE username =%(username)s', {'username': name})
myresult = mycursor.fetchone()

if myresult != 0:
    print('user exists')
# mydb.commit()
