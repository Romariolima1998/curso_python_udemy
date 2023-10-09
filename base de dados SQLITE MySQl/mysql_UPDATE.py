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

        tabela = cursor.fetchall()

        for row in tabela:
            print(row)
        print()

    # UPDATE aualizando os dados
    # CUIDADO COM UPDATE SEM WHERE
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {table_name} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s '
        )
        cursor.execute(sql, ('brenda', 20, 1))
        connection.commit()

    with connection.cursor() as cursor:
        # lendo toda a lista e todas colunas
        sql = (
            f'SELECT * FROM {table_name} '
        )
        cursor.execute(sql)

        tabela = cursor.fetchall()

        for row in tabela:
            print(row)
