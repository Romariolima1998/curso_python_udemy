
class Veiculo():
    def __init__(self,_,fabricante,modelo,ano,*args):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self._estado = False

    def ligar(self):
        if self._estado:
            print (self.modelo,' ja esta ligada')

        else:
            self._estado = True
            print (self.modelo,' ligada')

    def desligar (self):
        if self._estado == False:
            print (self.modelo,'ja esta desligada')

        else:
            self._estado = False
            print ( self.modelo,'desligado')

        
class Moto(Veiculo):
    def __init__(self,*args,**kwargs):
        self.tipo = args[0]
        super().__init__(*args,**kwargs)

    def acelerar(self):
        if self._estado == False:
            print('o veiculo esta desligado')

        else:
            print(self.tipo,'esta acelerando')


class Carro(Veiculo):
    def __init__(self,*args,**kwargs):
        self.tipo = args[0]
        super().__init__(*args,**kwargs)

    def acelerar(self):
        if self._estado == False:
            print('o veiculo esta desligado')

        else:
            print(self.tipo,'esta acelerando')


moto1 = Moto('motocicleta','honda','cg titan',1999)
carro1 = Carro('automovel','fiat','siena',2009)

moto1.ligar()
moto1.acelerar()

carro1.acelerar()
carro1.desligar()