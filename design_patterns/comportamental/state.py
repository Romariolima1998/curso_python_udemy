from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print(' tentando executar pending')
        self.state.pending()
        print('estado atual', self.state)
        print()

    def approve(self) -> None:
        print(' tentando executar approve')
        self.state.approve()
        print('estado atual', self.state)
        print()

    def reject(self) -> None:
        print(' tentando executar reject')
        self.state.reject()
        print('estado atual', self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):

    def pending(self) -> None:
        print('pagamento ja pendente, nao posso fazer nada')

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('pagamento aprovado')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('pagamento recusado')


class PaymentApproved(OrderState):

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('pagamento pendente')

    def approve(self) -> None:
        print('pagamento ja aprovado, nao posso fazer nada')

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('pagamento recusado')


class PaymentRejected(OrderState):

    def pending(self) -> None:
        print('pagamento recusado, nao posso mover para pendente')

    def approve(self) -> None:
        print('pagamento ja recusado, nao posso aprovar')

    def reject(self) -> None:
        print('pagamento recusado, nao posso recusar novamente')


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
