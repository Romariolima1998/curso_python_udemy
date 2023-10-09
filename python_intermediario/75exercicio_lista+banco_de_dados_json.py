import os
import json

def ler (tarefas, caminho):
    try:
        with open(caminho, 'r', encoding= 'utf8') as base_de_dados:
            dados = json.load(base_de_dados)

    except FileNotFoundError:
        salvar(tarefas, caminho)
        return tarefas
    return dados

def salvar (tarefas, caminho):
    with open (caminho, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas,arquivo, indent=2, ensure_ascii= False )
    return dados



caminho = 'lista.json'
tarefas =ler([],caminho)
lista_desfazer = []
ler(tarefas, caminho)

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
    
    salvar (tarefas,caminho)