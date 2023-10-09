
import random


cpf = ''
for _ in range(9):
    cpf += str(random.randrange(0,10))


nove_digitos = cpf[:9]
veses = 10
total = 0
for i in nove_digitos:
    total += int(i) * veses
    veses -= 1

divisao = (total * 10) % 11
resultado = 0 if divisao > 9 else divisao


nove_digitos1 = cpf[:9] + str(resultado)
veses2 = 11
total = 0
for i in nove_digitos1:
    total += int(i) * veses2
    veses2 -= 1

divisao2 = (total * 10) % 11
resultado2 = 0 if divisao2 > 9 else divisao2

resultado_final=str(resultado) + str(resultado2)
print(resultado_final)

cpf += str(resultado_final)
print (cpf)