# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

fmt = '%d/%m/%Y'

# data = datetime(2023, 7, 26, 12, 14)

data = datetime.strptime('2023-07-26 12:18:00', '%Y-%m-%d %H:%M:%S')

print(data)
print(data.strftime(fmt))

print(data.strftime('%d/%m/%Y %H:%M:%S'))
