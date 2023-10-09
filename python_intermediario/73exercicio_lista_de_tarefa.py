# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
'''
    COMANDOS: listar ADICIONAR desfazer refazer

'''
import os

tarefas =[]
lista_desfazer = []

def adicionar (tarefa):
    os.system('cls')
    tarefas.append(tarefa)
    print (tarefa)
    return None

def desfazer (tarefas):
    os.system ('cls')
    lista_desfazer.append(tarefas.pop())
    listar(tarefas)
    return None

def refazer(lista_desfazer):
    os.system('cls')
    tarefas.append(lista_desfazer.pop())
    listar(tarefas)
    return None

def listar (tarefas):
    os.system('cls')
    if len(tarefas) == 0:
        print ('lista vazia ')
        return 
    print ('......................tarefas......................')
    for indice,item in enumerate(tarefas):
        print (indice,' : ',item)




while True:
    
    print ('\n\n comandos: listar, adicionar, desfazer, refazer, sair')
    comando = input (' insira o comando desejado : ').lower()

    if comando == 'listar':
        listar(tarefas)

    elif comando == 'adicionar':
        while True:
            print (' digite (s) para sair de adicionar')
            adiciona =input('adicione uma tarefa..: ')
            if adiciona.lower() == 's':
                break
            adicionar(adiciona)
            listar(tarefas)
            

    elif comando == 'desfazer':
        desfazer(tarefas)  

    elif comando == 'refazer':
        refazer(lista_desfazer)

    elif comando == 'sair':
        print (' obrigado por usar a lista de tarefas ')
    
    else:
        print (' comando invalido')