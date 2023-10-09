'''Claro! Aqui está um desafio de programação em Python envolvendo polimorfismo:

Desafio:
Crie uma classe chamada Animal com um método chamado fazer_som().
 O método fazer_som() deve exibir uma mensagem genérica indicando o som feito pelo animal.

A seguir, crie três classes derivadas de Animal chamadas Cachorro, Gato e Vaca.
 Cada uma dessas classes deve ter seu próprio método fazer_som()
   que exibe uma mensagem específica indicando o som feito pelo respectivo animal.

Por fim, crie uma função chamada emitir_som() que recebe um objeto do tipo Animal
 como parâmetro e chama o método fazer_som() desse objeto.
   Essa função pode ser usada para testar o polimorfismo, pois será capaz de chamar o método apropriado,
     dependendo do tipo de animal passado como argumento. '''

from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,som) -> None:
        self.som_animal = som

    @abstractmethod
    def fazer_som(self) -> str:
        ...

class Cachorro (Animal):
    def fazer_som(self) ->str:
        print (f'o cachorro faz {self.som_animal}')

class Gato (Animal):
    def fazer_som(self) ->str:
        print (f'o cachorro faz {self.som_animal}')

def emitir_som(som:Animal):
    som.fazer_som()
    return

emitir_som(Cachorro('au au'))
emitir_som(Gato('meaw'))

