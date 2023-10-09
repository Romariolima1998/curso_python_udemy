
def criador_de_decorador (operador):

    def decorador (func):

        def interna (*args,**kwargs):
            
            if operador == 'soma':
                soma = int()
                for i in args:
                    soma += i
                return soma
        return interna
    return decorador
            
@criador_de_decorador(operador='soma')
def numeros (args):
    return args

teste = numeros(10,2,1)

print(teste)
            
            #if operador == 'divisao':
                #divisao
