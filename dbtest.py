import pymysql
from config import *

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=db_user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('db connect')
except Exception as ex:
    print('Error db connect...')
    print(ex)

login = "'" + input('login>') + "'"
password = "'" + input('password>') + "'"

with connection.cursor() as cursor:
    query = 'INSERT INTO test VALUES ({},{})'.format(login, password)
    cursor.execute(query)
    connection.commit()
