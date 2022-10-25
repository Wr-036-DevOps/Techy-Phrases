import mysql.connector
import variables
mydb = mysql.connector.connect(
    host=variables.host,
    user=variables.user,
    password=variables.password,
    database=variables.database
    )  
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE phrasedb")