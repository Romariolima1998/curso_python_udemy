from __future__ import annotations
from typing import Any, Dict, List
from copy import deepcopy


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__('_state', state)

    def get_satate(self) -> Dict:
        return self._state

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError('Sorry, i am immutable')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_satate()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if self._mementos:
            self._originator.restore(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor('foto1', 111, 111)
    caretaker = Caretaker(img)

    caretaker.backup()

    img.width = 222
    img.height = 222
    caretaker.backup()

    img.width = 333
    img.height = 333
    caretaker.backup()

    img.width = 444
    img.height = 444

    print(img)

    caretaker.restore()
    print(img)

    caretaker.restore()
    print(img)
