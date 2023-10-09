import sqlite3
from sqlite_INTO_CREATE import db_file, table_name

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# ler toda a database
cursor.execute(f' SELECT * FROM {table_name}')

# exibe os itens da tabela
for row in cursor.fetchall():
    _id, nome, peso = row
    print(_id, nome, peso)

# ler apenas 1 pelo id
cursor.execute(f' SELECT * FROM {table_name} '
               'WHERE id = "1"')

# exibe apenas um item da tabela
_id, nome, peso = cursor.fetchone()
print(_id, nome, peso)

# ler apenas 1 coluna
cursor.execute(f' SELECT nome FROM {table_name}')

# exibe apenas um item da tabela
row = cursor.fetchall()
print(row)

cursor.close()
connection.close()
