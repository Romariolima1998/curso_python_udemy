
# tipos de dados das tabelas
# https://dev.mysql.com/doc/refman/8.0/en/data-types.html

sql_users = ('CREATE TABLE base_de_dados.users ('
	'id INT UNSIGNED auto_increment NOT NULL,'
	'first_name varchar(150) NOT NULL,'
	'last_name varchar(150) NULL,'
	'email varchar(200) NOT NULL,'
	'password_hash varchar(255) NOT NULL,'
    'created_at DATETIME DEFAULT NOW() NOT NULL '
    'update_at DATETIME DEFAULT now() on update now() NOT NULL '
	'CONSTRAINT users_PK PRIMARY KEY (id),'
	'CONSTRAINT users_UN_email UNIQUE KEY (email),'
	'CONSTRAINT password_hash UNIQUE KEY (password_hash)'
')'
)

sql_roles = (
    'CREATE TABLE base_de_dados.roles ('
	'id INT UNSIGNED auto_increment NOT NULL,'
	'name varchar(100) NOT NULL,'
	'CONSTRAINT roles_PK PRIMARY KEY (id)'
')'
)

sql_user_role = (
    'CREATE TABLE base_de_dados.users_roles ('
	'user_id INT UNSIGNED NOT NULL,'
	'role_id INT UNSIGNED NOT NULL,'
	'CONSTRAINT users_roles_PK PRIMARY KEY (user_id,role_id),'
	'CONSTRAINT users_roles_FK FOREIGN KEY (user_id) REFERENCES base_de_dados.users(id) ON DELETE CASCADE ON UPDATE CASCADE,'
	'CONSTRAINT users_roles_FK_1 FOREIGN KEY (role_id) REFERENCES base_de_dados.roles(id) ON DELETE CASCADE ON UPDATE CASCADE'
')'
)

sql_profiles = (
    'CREATE TABLE base_de_dados.profiles ('
	'id INT UNSIGNED auto_increment NOT NULL,'
	'Column1 TEXT NULL,'
	'description TEXT NULL,'
	'user_id INT UNSIGNED NULL,'
	'CONSTRAINT profiles_PK PRIMARY KEY (id),'
    'CONSTRAINT profiles_UN UNIQUE KEY (user_id) '
	'CONSTRAINT profiles_FK FOREIGN KEY (user_id) REFERENCES base_de_dados.users(id) ON DELETE CASCADE ON UPDATE CASCADE'
')'
)