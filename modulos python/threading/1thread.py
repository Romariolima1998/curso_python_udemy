from threading import Thread
import time


class MeuThread(Thread):
    def __init__(self, texto: str, tempo: int) -> None:
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self) -> None:
        time.sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('thread1', 5)
t1.start()

for i in range(20):
    print(i)
    time.sleep(1)

