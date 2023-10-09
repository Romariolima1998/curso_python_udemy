# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
'''
%a > Dias da semana como nomes abreviados da localidade.
Sun, Mon, …, Sat (en_US);
So, Mo, …, Sa (de_DE)
(1)

%A > Dia da semana como nome completo da localidade.
Sunday, Monday, …, Saturday (en_US);
Sonntag, Montag, …, Samstag (de_DE)
(1)

%w > Dia da semana como um número decimal, onde 0 é domingo e 6 é sábado.
0, 1, …, 6

%d > Dia do mês como um número decimal com zeros a esquerda.
01, 02, …, 31
(9)

%b > Mês como nome da localidade abreviado.
Jan, Feb, …, Dec (en_US);
Jan, Feb, …, Dez (de_DE)
(1)

%B > Mês como nome completo da localidade.
January, February, …, December (en_US);
janeiro, fevereiro, …, dezembro (pt_BR)
(1)

%m > Mês como um número decimal com zeros a esquerda.
01, 02, …, 12
(9)

%y > Ano sem século como um número decimal com zeros a esquerda.
00, 01, …, 99
(9)

%Y > Ano com século como um número decimal.
0001, 0002, …, 2013, 2014, …, 9998, 9999
(2)

%H > Hora (relógio de 24 horas) como um número decimal com zeros a esquerda.
00, 01, …, 23
(9)

%I > Hora (relógio de 12 horas) como um número decimal com zeros a esquerda.
01, 02, …, 12
(9)

%p > Equivalente da localidade a AM ou PM.
AM, PM (en_US);
am, pm (de_DE)
(1), (3)

%M > Minutos como um número decimal, com zeros a esquerda.
00, 01, …, 59
(9)

%S > Segundos como um número decimal, com zeros a esquerda.
00, 01, …, 59
(4), (9)

%f > Microssegundos como um número decimal, com zeros à esquerda até completar 
6 dígitos.

000000, 000001, …, 999999

(5)
'''

from datetime import date, time
from datetime import datetime

data_str_data = '20/04/2022 07:49:23'
data_str_fmt = '%d/%m/%Y %H:%M:%S'

data1 = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)


datas = date(2023, 7, 25)
hora = time(13, 21)
print(datas, hora)
