# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro():
    def __init__(self,nome) -> None:
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,motor):
        self._motor = motor
        return
    

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,fabricante):
        self._fabricante = fabricante
        
    
    def listar(self):
        print (self.nome, self._fabricante.nome, self._motor.nome)
        return
    
class Motor():
    def __init__(self,nome):
        self.nome = nome

class Fabricante():
    def __init__(self,nome):
        self.nome = nome

f1 = Fabricante('wolkiswagem')
m1 = Motor('AP')
carro1 = Carro('gol')
carro1.fabricante = f1
#carro1.motor = m1
carro1.listar()
