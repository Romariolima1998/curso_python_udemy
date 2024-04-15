from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    '''componente'''

    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    '''composite'''

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    '''leaf'''

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    camiseta1 = Product('camiseta1', 19.99)
    camiseta2 = Product('camiseta2', 17.99)
    camiseta3 = Product('camiseta3', 199.99)

    caixa_de_camiseta = Box('caixa de camiseta')
    caixa_de_camiseta.add(camiseta1)
    caixa_de_camiseta.add(camiseta2)
    caixa_de_camiseta.add(camiseta3)

    caixa_de_camiseta.print_content()
    print(caixa_de_camiseta.get_price())

    xiaomi = Product('note 13', 5000.50)

    caixa_de_smartphones = Box('caixa de smartphones')
    caixa_de_smartphones.add(xiaomi)

    caixa_grande = Box('caixa grande')
    caixa_grande.add(caixa_de_camiseta)
    caixa_grande.add(caixa_de_smartphones)

    caixa_grande.print_content()
    caixa_grande.get_price()
