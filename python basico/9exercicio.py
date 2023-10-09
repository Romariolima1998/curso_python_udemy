"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# inserir a palavra secreta
palavra_secreta = input(' insira uma palavra secreta..: ')

# exibir quantas letras tem
qtd_de_letras = len(palavra_secreta)
resultado_palavra = qtd_de_letras * ['*']

erros = 0
acertos =0

while erros != 5:
    if acertos == len(palavra_secreta):
        print (f'\n {palavra_secreta} \n')
        print ('voce venceu parabens')
        break

    print (f'{resultado_palavra}  {qtd_de_letras} letras e {erros} erros')

#pedir letra
    letra = input('insira uma letra..: ')
    if len(letra) >= 2:
        print ( 'apenas um caracter por vez')
        continue
#verificar se sao iguais, se sim exiba no local
#se nao adicione 1 aos erros
    posicao = 0
    for i in palavra_secreta:
        if letra == i:
            resultado_palavra[posicao] = letra
            posicao +=1
            acertos += 1   
        else:
            posicao +=1
    posicao = 0

    if letra not in palavra_secreta:
        erros += 1
    
else:
    print (' voce perdeu')
            
