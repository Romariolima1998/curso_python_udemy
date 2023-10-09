# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

import pymysql
import pymysql.cursors
import dotenv
import os

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor
)

table_name = 'customers'

with connection:
    with connection.cursor() as cursor:
        # lendo toda a lista e todas colunas
        sql = (
            f'SELECT * FROM {table_name} '
        )
        dados_tabela = cursor.execute(sql)

        tabela = cursor.fetchall()

        for row in tabela:
            print(row)
        print()
        print(dados_tabela)
        print(len(tabela))
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)  # primeirovalor inserido da ultima inserçao

        cursor.execute(
            f'SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1'
        )
        print('ultimo id', cursor.fetchone())
        print('rownumber', cursor.rownumber)  # mostra em qual linha seu cursor esta
