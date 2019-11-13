from django.db import models

# Create your models here.
import mysql.connector
# Import my database from mysql
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "marom317",
    database = "workdb"
)
print(mydb)
mycursor = mydb.cursor()
# fun with all my data as a tuple
def get_all_data():
    mycursor.execute("SELECT * FROM workers ")
    return mycursor.fetchall()
