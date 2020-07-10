# install mysql-connector-python and mysql.connector
import mysql.connector


mydb = mysql.connector.connect(host='127.0.0.1', user='****', password='****', database='testdb')
print(mydb)
# , auth_plugin='mysql_native_password'
# , database="testdb"
# creating a DB with a cursor. Cursor is an object that communicates with the entire mysql server
# initialize cursor

mycursor = mydb.cursor()

# mycursor.execute('CREATE DATABASE testdb')   # create DB
# mycursor.execute("CREATE TABLE Students(name VARCHAR(255), age INTEGER(10))")  # create table students


mycursor.execute('SHOW DATABASES')  # lists all DBs
for db in mycursor:    # lists all DB
    print(db)

mycursor.execute("SHOW TABLES")  # lists the tables
for tb in mycursor:
    print('tables in testdb: ', tb)

# populate database and tables
sqlFormula = "INSERT INTO Students(name,age) VALUES (%s, %s)"
student1 = ("Rachel", 22)

mycursor.execute(sqlFormula, student1)
mydb.commit() # saves changes to the DB


mydb.close()
