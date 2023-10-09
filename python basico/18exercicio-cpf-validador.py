"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
cpf = '746.824.890-70'
lista_cpf = cpf.split(".")
correcao = lista_cpf[2].split('-')
lista_cpf.append(correcao[0])
lista_cpf.pop(-2)
print (lista_cpf)

veses = 10
total_soma = 0
for item in lista_cpf:
    for i in item:
        total_soma += (int(i) * veses)
        veses -=1

divisao =(total_soma * 10) % 11

resultado = 0 if divisao > 9 else divisao

print (resultado)

#segundo digito

cpf2 = '74682489070'

nove_digitos = cpf2[:9] + str(resultado)
veses2 = 11
total = 0
for i in nove_digitos:
    total += int(i) * veses2
    veses2 -= 1

divisao2 = (total * 10) % 11
resultado2 = 0 if divisao2 > 9 else divisao2

resultado_final=str(resultado) + str(resultado2)
print(resultado_final)