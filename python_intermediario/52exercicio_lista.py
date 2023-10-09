# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper (lista_cidade,lista_estado):
    lista_completa = [(item,lista_estado[i])for i,item in enumerate(lista_cidade)]
    return lista_completa

lista_completa = zipper(cidade,estado)
print (lista_completa)

