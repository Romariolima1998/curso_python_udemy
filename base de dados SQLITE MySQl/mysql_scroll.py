# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql
import dotenv
import os

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

table_name = 'customers'

with connection:
    with connection.cursor() as cursor:
        # lendo toda a lista e todas colunas
        sql = (
            f'SELECT * FROM {table_name} '
        )
        cursor.execute(sql)

        for row in cursor.fetchall():
            print(row)
        print()

        print(cursor.fetchone(), 'essa posiçao nao mostra porque'
              ' o cursor se esgotou')
        print()

        # scroll pode voutar 1 casa apartir da posiçao atual
        cursor.scroll(-1)
        print(cursor.fetchone())
        print()

        # ou voltar ate a posiçao desejada
        cursor.scroll(0, 'absolute')
        for row in cursor.fetchall():
            print(row)
        print()
