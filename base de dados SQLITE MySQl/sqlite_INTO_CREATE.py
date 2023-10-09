# documentaçao  https://www.sqlite.org/doclist.html
# CRUD = Create         Reade   Update  Delete
# sql - insert create   select  update   delete
import sqlite3
from pathlib import Path

db_name = 'db.sqlite3'
root_dir = Path(__file__).parent
db_file = root_dir / db_name
table_name = 'cliente'

# criando conexao com o arquivo sqlite3
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# criando tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {table_name}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
    ')'
)
connection.commit()

# CUIDADO: fazendo delete sem WHERE apagar tudo
cursor.execute(
    f'DELETE FROM {table_name}'
)
connection.commit()

# zerar a sequencia
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{table_name}"'
)
connection.commit()

# registra valores nas colunas das tabelas
# cuidado com sql injection
sql = (f'INSERT INTO {table_name} (nome, peso) '
'VALUES'
' (?, ?)')


# apenas 1 valor
# cursor.execute(sql, ["Romario", 63])

# varios valores de uma vez
# cursor.executemany(sql, (("joana", 50), ("luiz", 70)))

# trabalhando com dicionarios
sql = (f'INSERT INTO {table_name} (nome, peso) '
'VALUES'
' (:nome, :peso)'
) # de acordo com as chaves do dicionario

cursor.execute(sql, {'nome': "Romario", 'peso': 63})

cursor.executemany(
    sql,
    [
        {'nome': 'fulano', 'peso': 50},
        {'nome': 'ciclano', 'peso': 50},
        {'nome': 'bertano', 'peso': 50}
    ]
)
connection.commit()

if __name__ == '__main__':
    cursor.execute(
        f'DELETE FROM {table_name}'
        ' WHERE id = "3"'
    )
    connection.commit()

# exibe os valores da coluna
    cursor.execute(
        f'SELECT * FROM {table_name}'
    )
    for row in cursor.fetchall():
        _id, nome, peso = row
        print(_id, nome, peso)

# atualiza os dados de um bloco de uma coluna
    cursor.execute(
        f'UPDATE {table_name} '
        'SET nome = "novo nome", peso = 69 '
        'WHERE id = 2'
    )
    connection.commit()

    print()
    # exibe os valores da coluna
    cursor.execute(
        f'SELECT * FROM {table_name}'
    )
    for row in cursor.fetchall():
        _id, nome, peso = row
        print(_id, nome, peso)

    cursor.close()
    connection.close()
