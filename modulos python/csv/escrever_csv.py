from pathlib import Path
import csv

caminho_csv = Path(__file__).parent / '2csv.csv'

lista_cliente = [
    {'nome': 'romario', 'cidade': 'linhares'},
    {'nome': 'alguem', 'cidade': 'qualquer'}
]

with open(caminho_csv, 'w', encoding='utf8') as arquivo:
    escritor = csv.writer(arquivo)
    colunas = lista_cliente[0].keys()

    escritor.writerow(colunas)

    for lista in lista_cliente:
        escritor.writerow(lista.values())


lista_cliente = [
    ['nome', 'cidade'],
    ['romario', 'linhares'],
    ['alguem', 'qualquer']
]

with open(caminho_csv, 'w', encoding='utf8') as arquivo:
    escritor = csv.writer(arquivo)

    for lista in lista_cliente:
        escritor.writerow(lista)


lista_cliente = [
    {'nome': 'romario', 'cidade': 'linhares'},
    {'nome': 'alguem', 'cidade': 'qualquer'}
]

with open(caminho_csv, 'w', encoding='utf8') as arquivo:
    colunas = lista_cliente[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)

    escritor.writeheader()

    for lista in lista_cliente:
        print(lista)
        escritor.writerow(lista)