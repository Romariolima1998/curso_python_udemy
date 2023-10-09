import contas
import pessoa


class Banco():
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoa.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta: contas.Conta) -> bool:
        if conta.agencia in self.agencias:
            return True
        print('agencia nao e do banco')
        return False

    def _checa_cliente(self, cliente: pessoa.Cliente) -> bool:
        if cliente in self.clientes:
            return True
        print('cliente nao e do banco')
        return False

    def _checa_conta(self, conta: contas.Conta) -> bool:
        if conta in self.contas:
            return True
        print('conta nao e do banco')
        return False

    def _checa_conta_do_cliente(
            self,
            cliente: pessoa.Cliente,
            conta: contas.Conta
    ) -> bool:
        if cliente.conta == conta:
            return True
        print('conta nao e do cliente')
        return False

    def autenticar(self, conta: contas.Conta, cliente: pessoa.Cliente) -> bool:
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_conta_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r},{self.clientes!r},{self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = pessoa.Cliente('joao', 30)
    cc1 = contas.ContaCorrente(222, 222, 0, 100)
    c1.conta = cc1

    c2 = pessoa.Cliente('ana', 30)
    cp2 = contas.ContaPoupanca(221, 221, 50)
    c2.conta = cp2

    banco1 = Banco()
    banco1.clientes.extend([c1, c2])
    banco1.contas.extend([cc1, cp2])
    banco1.agencias.extend([222, 221])

    print(banco1.autenticar(cp2, c2))

    print(banco1)
