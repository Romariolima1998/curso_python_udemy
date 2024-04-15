from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, collegue: Colleague, msg: str) -> None: pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None: pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self.collegue: List[Colleague] = []

    def is_collegue(self, collegue: Colleague) -> bool:
        return collegue in self.collegue

    def add(self, collegue: Colleague) -> None:
        if not self.is_collegue(collegue):
            self.collegue.append(collegue)

    def remove(self, collegue: Colleague) -> None:
        if self.is_collegue(collegue):
            self.collegue.remove(collegue)

    def broadcast(self, collegue: Colleague, msg: str) -> None:
        if self.is_collegue(collegue):
            print(f'{collegue.name} disse: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if self.is_collegue(sender):
            receiver_obj: List[Colleague] = [
                collegue for collegue in self.collegue
                if collegue.name == receiver
            ]

            if receiver_obj:
                receiver_obj[0].direct(
                    f'{sender.name} para {receiver_obj[0].name}: {msg}'
                )


if __name__ == '__main__':
    chat = Chatroom()

    romario = Person('romario', chat)
    rin = Person('rin', chat)
    kakashi = Person('kakashi', chat)
    kasuma = Person('kasuma', chat)

    chat.add(romario)
    chat.add(rin)
    chat.add(kasuma)

    kasuma.broadcast('iae guys, blz')
    romario.send_direct('kasuma', 'fala viado')
