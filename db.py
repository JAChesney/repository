from mysql import connector
from mysql.connector.plugins import caching_sha2_password

dataBase = connector.connect(
    host = 'localhost',
    user = 'root',
    password = "*222bda03jason*",
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute('create database if not exists repodb')

print('All done!')