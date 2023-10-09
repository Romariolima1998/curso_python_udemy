
"""
enumerate - enumera iteráveis ​​(índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista  = [ 'Maria' , 'Helena' , 'Luiz' ]
lista . anexar ( 'João' )

for  indice , nome  in  enumerate ( lista ):
    print ( indice , nome , lista [ índice ] )

# para item em enumerate(lista):
# índice, nome = item
# print(índice, nome)


# para tupla_enumerada em enumerate(lista):
# print('PARA tupla:')
# para valor em tupla_enumerada:
# print(f'\t{valor}')