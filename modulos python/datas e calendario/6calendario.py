# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar
# calendario completo
# print(calendar.calendar(2022))

# calendario do mes
print(calendar.month(2022, 12))

# numero que simboliza o primeiro dia da semana ex 0=segunda, ultimo dia do ano
# numero_primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)

# qual nmr simboliza qual dia ex: 0=seg 1=ter
# print(list(enumerate(calendar.day_name)))

# pega o dia da semana pelo numero ex 0=seg
# print(calendar.day_name[numero_primeiro_dia])

# pega o (nome)dia da semana pelo dia do mes ex: dia 30 = sabado
# print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)])
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)
