"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod
import random


class Conta(ABC):
    @abstractmethod
    def _saque(self, valor) -> None:
        pass


class ContaPoupanca(Conta):
    def __init__(self) -> None:
        self._agencia = 1
        self._conta = random.randrange(10, 100)
        self._saldo = 0

    def _deposito(self, valor) -> None:
        self._saldo += valor
        return

    def _saque(self, valor) -> None:
        if self._saldo < valor:
            print('saldo insuficiente')
            return
        self._saldo -= valor
        print(
            f'saque de {valor} efetuado com sucesso, seu saldo agora e de {self._saldo}')
        return


class ContaCorrente(Conta):

    def __init__(self) -> None:
        self._agencia = 1
        self._conta = random.randrange(10, 100)
        self._saldo = 0
        self._saldo_credito = 100

    def _deposito(self, valor) -> None:
        self._saldo += valor
        return

    def _saque(self, valor) -> None:
        if self._saldo < valor:
            self._saldo += self._saldo_credito
            self._saldo_credito = -100
            if self._saldo < valor:
                print('saldo insuficiente')
                return
        self._saldo -= valor
        print(
            f'saque de {valor} efetuado com sucesso, seu saldo agora e de {self._saldo}')
        return


class Banco ():
    def __init__(self) -> None:
        self._cliente = []
        self._contas = []

    def _add_client(self, cliente):
        self._cliente.append(cliente)


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.conta = None


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        self.banco = None
        self.conta = None
        super().__init__(nome, idade)

    def deposito(self, valor: int | float) -> None:
        if self.conta == None:
            print('voce ainda nao possui uma conta')
            return
        self.conta._deposito(valor)

    def saque(self, valor: int) -> None:
        if self.conta == None:
            print('voce ainda nao possui uma conta')
        self.conta._saque(valor)

    def set_banco(self, banco: Banco):
        self.banco = banco
        banco._add_client(self)

    def criar_conta(self, tipo: str):
        if self.banco == None:
            print('escolha um banco primeiro')
            return
        if tipo not in ['corrente', 'poupanca']:
            print('apenas conta corrente e poupança')
            return
        elif tipo == 'corrente':
            self.conta = ContaCorrente()
        else:
            self.conta = ContaPoupanca()
        self.banco._contas.append(self.conta)


caixa = Banco()
romario = Cliente('romario', 25)
romario.set_banco(caixa)
romario.criar_conta('corrente')

# romario.conta.__new__(ContaCorrente)

romario.deposito(100)
romario.saque(100)

pessoa = Cliente('pessoa', 30)
pessoa.set_banco(caixa)

pessoa.criar_conta('poupanca')
pessoa.saque(50)

romario.saque(150)
romario.saque(50)
