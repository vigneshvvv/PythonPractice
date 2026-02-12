import mysql.connector
from mysql.connector import Error

def mySqlConnect():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            database = "javatrainingpro",
            user = "root",
            password = ""
        )

        if connection.is_connected():
            print("connection established")
            cursor = connection.cursor()
            selectQuery = "select * from books"
            cursor.execute(selectQuery)
            result = cursor.fetchall()
            print(result)
    except Error as e:
        print(e)
    finally:
        # if connection.is_connected():
            # cursor.close()
            # connection.close()    
        print("finally executed")    


mySqlConnect()
