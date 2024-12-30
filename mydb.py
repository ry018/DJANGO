import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'RUPESH',
    passwd = 'MSQLpassword@123',
)

cursor_object = db.cursor()

cursor_object.execute("CREATE DATABASE crmdb")
print("All done!")
