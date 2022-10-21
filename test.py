import mysql.connector
import variables

mydb = mysql.connector.connect(
    host=variables.host,
    user=variables.user,
    password=variables.password,
    database=variables.database
    )   

mycursor = mydb.cursor()

mycursor.execute("Select * from $TABLE NAME ")

for x in mycursor:
    print(x)