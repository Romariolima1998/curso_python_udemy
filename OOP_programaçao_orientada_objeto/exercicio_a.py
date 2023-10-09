# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
pasta = 'curso de python udemy/OOP_programaçao_orientada_objeto/aula9oop.json'

class Carro ():
    def __init__(self,consecionaria,modelo,cor,cilindrada):
        self.consecionaria = consecionaria
        self.modelo = modelo
        self.cor = cor
        self.cilindrada = cilindrada

carro1 = Carro('fiat','uno way','cinza',1.0)

with open(pasta,'w',encoding='utf-8') as arquivo:
    json.dump(vars(carro1),arquivo,indent=2, ensure_ascii=False)