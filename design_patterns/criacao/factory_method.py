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


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('moto popular esta buscando o cliente')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('moto de luxo esta buscando o cliente')


# factory
class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()

        elif tipo == 'popular':
            return CarroPopular()

        elif tipo == 'moto':
            return MotoPopular()

        elif tipo == 'moto_luxo':
            return MotoLuxo()

        assert 0, 'veiculo nao existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()

        assert 0, 'veiculo nao existe'


if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_disponiveis_zona_sul = ['popular']

    for i in range(10):
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print('---------------------')

    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
