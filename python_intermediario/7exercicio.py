
numeros = 1, 5, 6, 7, 8
print ( 1 * 5 * 6 * 7 * 8)

def multiplicacao(*args):
    total = 1

    for i in args:
        total *= i
    return total

print (multiplicacao(*numeros))

#par ou impar

def par_ou_impar (numero):
    return 'par' if numero % 2 == 0 else 'impar'

print (par_ou_impar(multiplicacao(*numeros)))