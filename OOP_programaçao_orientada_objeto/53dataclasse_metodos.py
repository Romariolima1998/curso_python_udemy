from dataclasses import dataclass


@dataclass
class Pessoa():
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor: str):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('joao', 'figueredo')

    p1.nome_completo = 'romario lima'

    print(p1)
