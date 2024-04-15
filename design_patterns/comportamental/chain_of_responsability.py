from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handler(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['A', 'B', 'C']

    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerABC: conseguiu tratar o valor {letter}'
        return self.sucessor.handler(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['D', 'E', 'F']

    def handler(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerDFG: conseguiu tratar o valor {letter}'
        return self.sucessor.handler(letter)


class HandlerUnsolved(Handler):

    def handler(self, letter: str) -> str:
        return f'HandlerUnsolved: Nao tratou o valor {letter}'


if __name__ == '__main__':
    hendler_unsolved = HandlerUnsolved()
    hendler_def = HandlerDEF(hendler_unsolved)
    hendler_abc = HandlerABC(hendler_def)

    print(hendler_abc.handler('A'))
    print(hendler_abc.handler('E'))
    print(hendler_abc.handler('H'))
