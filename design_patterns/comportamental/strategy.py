from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float) -> None:
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == '__main__':
    no_discount = NoDiscount()
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()

    five_percent = CustomDiscount(5)

    order = Order(1000, no_discount)
    print(order.total, order.total_with_discount)

    order = Order(1000, twenty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, fifty_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, five_percent)
    print(order.total, order.total_with_discount)

    order = Order(1000, CustomDiscount(1))
    print(order.total, order.total_with_discount)
