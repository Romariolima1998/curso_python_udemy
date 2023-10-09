# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql
import dotenv
import pymysql.cursors
import os

dotenv.load_dotenv()
# nao funciona scroll e pega um valor cada vez 
# apeas para base de dados muito pesadas

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.SSDictCursor,
)

table_name = 'customers'

with connection:
    with connection.cursor() as cursor:
        # lendo toda a lista e todas colunas
        sql = (
            f'SELECT * FROM {table_name} '
        )
        cursor.execute(sql)

        for row in cursor.fetchall_unbuffered():
            print(row)
        print()
