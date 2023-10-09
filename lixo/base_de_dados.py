import pymysql

connection = pymysql.connect(
    host='localhost',
    user='usuario',
    passwd='senha',
    database='base_de_dados'
)

sql = (
    'select u.id, u.first_name, r.name '
    'from users as u '
    'left join users_roles as ur '
    'on u.id = ur.user_id '
    'inner join roles as r '
    'on ur.role_id = r.id '
    'order by u.id desc '
    'limit 10'
)
with connection:
    with connection.cursor() as cursor:
        cursor.execute(sql)

        tabela = cursor.fetchall()

        for coluna in tabela:
            print(*coluna)
