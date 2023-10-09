# Exercício - sistema de perguntas e respostas

import os
import time
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for item in perguntas:
    print (item['Pergunta'])
    print('....opções....')
    for i in item['Opções']:
        print (' ',i)

    resposta = input ('\n insira sua resposta..: ')
    while resposta not in item['Opções']:
        print('\n  resposta invalida apenas :',item['Opções'])
        resposta = input ('\n insira sua resposta..: ')

    if resposta == item['Resposta']:
        print (' \n .........voce acertou..........')
        acertos += 1
    else:
        print (' \n ........voce errou.........')

    time.sleep(5)
    os.system('cls')

if acertos  < 1:
    print (' iiiiiii burrão errou tudo kkkkkk.....')

else:
    print(f'parabens voce acertou {acertos} de {len(perguntas)}')
    
        
    