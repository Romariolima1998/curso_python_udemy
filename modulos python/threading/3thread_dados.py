from threading import Thread
from threading import Lock
from time import sleep


class ingressos:
    def __init__(self, estoque: int) -> None:
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade: int):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('nao temos ingressos sulficiente')
            self.lock.release()
            return
        sleep(1)
        self.estoque -= quantidade
        print(f'voce comprou {quantidade} ingressos, restam {self.estoque} ingresso(s)')
        self.lock.release()


if __name__ == '__main__':
    ingressos = ingressos(10)

    for i in range(1, 20):
        t1 = Thread(target=ingressos.comprar(i))
        t1.start()
    print(ingressos.estoque)