from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from copy import deepcopy
from dataclasses import dataclass

# ingredients


@dataclass
class Ingredient:
    price: float

    def __str__(self) -> str:
        return self.__class__.__name__


@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoesSticks(Ingredient):
    price: float = 0.99

# hotdogs


class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name} {self.price} {self.ingredients}'


class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'Simple Hotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            PotatoesSticks()
        ]


class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name = 'Simple Hotdog'
        self._ingredients = [
            Bread(),
            Sausage(),
            PotatoesSticks(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes()
        ]

# decoratos


class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.hotdog._ingredients


class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)
        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    # ---------com decorator unico-------------------


class UHotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient
        self._ingredients = deepcopy(self.hotdog._ingredients)
        self.ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


if __name__ == '__main__':
    simple_hotdog = SimpleHotdog()
    print(simple_hotdog)

    special_hotdog = SpecialHotdog()
    print(special_hotdog)

    # ---decorators-------------------------
    bacon_simple_hotdog = BaconDecorator(simple_hotdog)
    print(bacon_simple_hotdog)

    # --com decorator unico---------------
    a_pedido_do_cliente = UHotdogDecorator(simple_hotdog, Bacon())
    print(a_pedido_do_cliente)
    print(a_pedido_do_cliente.price)
