from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: int | float) -> None:
        ...

    def depositar(self, valor: float) -> None:
        self.saldo += valor
        self.detalhes(f'deposito de {valor}')
        return

    def detalhes(self, msg: str) -> None:
        print(f' o seu saldo e de {self.saldo:.2f} {msg}')
        print('--')
        return

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r},{self.conta!r},{self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor: int | float) -> None:
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'saque de {valor}')
            return
        print('nao foi possivel sacar o valor desejado')
        self.detalhes(f'saldo insulficiente, saque negado de {valor}')


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: int | float, credito: int | float = 0) -> None:
        super().__init__(agencia, conta, saldo)
        self.credito = credito

    def sacar(self, valor: int | float) -> None:
        valor_pos_saque = self.saldo - valor
        credito = -self.credito
        if valor_pos_saque >= credito:
            self.saldo -= valor
            self.detalhes(f'saque de {valor}')
            return
        print('nao foi possivel sacar o valor desejado')
        self.detalhes(f'saldo insulficiente, saque negado de {valor}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r},{self.conta!r},{self.saldo!r},{self.credito!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    conta1 = ContaPoupanca(1, 222, 0)
    conta1.sacar(1)

    conta1.depositar(1)
    conta1.sacar(1)
    print('################################')
    cc = ContaCorrente(1, 222, 0, 100)
    cc.sacar(1)

    cc.depositar(1)
    cc.sacar(1)
