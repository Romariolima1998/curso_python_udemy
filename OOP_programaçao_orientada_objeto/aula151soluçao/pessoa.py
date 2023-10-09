import contas


class Pessoa():
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self) -> int:
        return self._idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r},{self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self._conta: contas.Conta | None = None

    @property
    def conta(self):
        return self._conta

    @conta.setter
    def conta(self, valor: contas.Conta):
        self._conta = valor


if __name__ == "__main__":

    c1 = Cliente('romario', 25)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)

    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    c2 = Cliente('ana', 25)
    c2.conta = contas.ContaPoupanca(111, 333, 0)
    print(c2)
    print(c2.conta)
