from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('carro de luxo esta buscando o cliente')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('carro popular esta buscando o cliente')

# factory 1


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()

        elif tipo == 'popular':
            return CarroPopular()

        assert 0, 'veiculo nao existe'


# factory 2
class VeiculoFactory2():
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()

        elif tipo == 'popular':
            return CarroPopular()
        assert 0, 'veiculo nao existe'

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == '__main__':
    from random import choice

    carros_disponiveis = ['luxo', 'popular']

# factory 1
    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()

# factory 2
    print('-------------------------------')
    for i in range(10):
        carro2 = VeiculoFactory2(choice(carros_disponiveis))
        carro2.buscar_cliente()
