"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista =['items']

while True:
    
    funcao = input(' [i]nserir, [a]pagar, [l]istar, [s]air: ').lower()
    if funcao != 'i' and funcao != 'a' and funcao != 'l' and funcao != 's':
        os.system('cls')
        print(' digite apenas (a) (i) ou (l)')
        continue

    if funcao == 'i':
        
        while 's' not in lista.lower():
            
            print ('pressione (s) para sair')
            lista.append(input('adicione um item..: '))
            os.system('cls')   
        lista.pop()
        

    if funcao == 'a': 
        for i, item in enumerate(lista):
            print(i,item)
        try:
            indice = int(input('digite o indice a ser apagado..: '))
            lista.pop(indice)
        except:
            print(' indice inesistente')
        os.system('cls')

    if funcao == 'l':
        for i, item in enumerate(lista):
            print(i,item)
        

    if funcao == 's':
        print('obrigado por usar a lista')
        break
    
