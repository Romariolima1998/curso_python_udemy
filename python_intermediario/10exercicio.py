# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro. 

def multiplicador (multiplicador):
    def operacao (numero):
        return multiplicador * numero
    return operacao

multiplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

print (multiplicar(5))
print (triplicar(5))
print (quadruplicar(5))
