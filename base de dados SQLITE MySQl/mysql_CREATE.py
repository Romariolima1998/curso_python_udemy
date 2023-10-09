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
        # criando tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {table_name} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # CUIDADO = limpa a tabela
        cursor.execute(f'TRUNCATE TABLE {table_name}')

    connection.commit()

# começo a manipular dados apartir daqui

    with connection.cursor() as cursor:

        # inserindo valores na tabela SUGEITO A SQLINJECTION
        result = cursor.execute(
            f'INSERT INTO {table_name} '
            '(nome, idade) VALUES '
            '("luiz", 25) '
        )
        print(result)

        # forma SEGURA contra sqlinjection

        sql = (
            f'INSERT INTO {table_name} '
            '(nome, idade) VALUES '
            '(%s, %s) '
            )

        cursor.execute(sql, ('romario', 25))

        # utilizando dicionario
        dicionario = {
            'chave_nome': 'daniel',
            'chave_idade': 17
            }

        sql = (
            f'INSERT INTO {table_name} '
            '(nome, idade) VALUES '
            '(%(chave_nome)s, %(chave_idade)s) '
            )

        cursor.execute(sql, dicionario)

        connection.commit()

# inserindo varios valores de uma vez
    with connection.cursor() as cursor:

        # forma SEGURA contra sqlinjection
        sql = (
            f'INSERT INTO {table_name} '
            '(nome, idade) VALUES '
            '(%s, %s) '
            )
        tabela = (
            ('artur', 99),
            ('romulo', 77),
            ('alguem', 40)
        )

        cursor.executemany(sql, tabela)

        # utilizando dicionario
        dicionario = (
            {'chave_nome': 'daniel', 'chave_idade': 17},
            {'chave_nome': 'rogerio', 'chave_idade': 18},
            {'chave_nome': 'alves', 'chave_idade': 19},
        )

        sql = (
            f'INSERT INTO {table_name} '
            '(nome, idade) VALUES '
            '(%(chave_nome)s, %(chave_idade)s) '
            )

        cursor.executemany(sql, dicionario)

        connection.commit()
