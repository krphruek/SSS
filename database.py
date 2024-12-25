import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="5905",
        database="mydb",
)

mycursor = mydb.cursor(dictionary=True)