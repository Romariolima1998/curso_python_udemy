from dataclasses import dataclass


@dataclass
class Pessoa():
    nome: str
    idade: int


if __name__ == '__main__':
    p1 = Pessoa('romario', 25)
    p2 = Pessoa('romario', 25)

    print(p1)
    print(p1 == p2)
