"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    nmr_int = int(input('insira um numero inteiro..:'))
    if nmr_int % 2 == 0:
        print (f'o numero {nmr_int} e par')
    else:
        print (f'o numero{nmr_int} e impar')
except:
    print ('nao e um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação coletiva. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input(' digite as horas nete formato.: 00.00 ....: ')
try:
    horas = float(entrada)
except:
    print (' formato incorreto')

if horas >= 0 and horas <= 11.59:
    print(' bom dia')
elif horas >= 12 and horas <= 18.59:
    print (' boa tarde')
elif horas >= 19:
    print ('boa noite')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input(' insira seu primeiro nome')

try:
    nome = str(nome)
except:
    print ('digite apenas nome')

nmr_nome = len(nome)

if nmr_nome <= 4 :
    print (' seu nome e curto')
elif nmr_nome >= 5 and nmr_nome <= 6:
    print (' seu nome e normal')
elif nmr_nome >= 7:
    print ('seu nome e grande')
