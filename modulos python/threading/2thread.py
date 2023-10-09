from threading import Thread
from time import sleep


def vai_demorar(texto: str, tempo: float):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('ola mundo', 5))
t1.start()


t2 = Thread(target=vai_demorar, args=('ola mundo', 7))
t2.start()


for i in range(20):
    print(i)
    sleep(.5)

    # ---------------------------------------
t3 = Thread(target=vai_demorar, args=('ola mundo', 10))
t3.start()

while t3.is_alive():
    print('esperando thread')
    sleep(2)
