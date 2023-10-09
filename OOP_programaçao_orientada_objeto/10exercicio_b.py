import exercicio_a
import json

pasta = 'curso de python udemy/OOP_programaçao_orientada_objeto/aula9oop.json'

with open(pasta, 'r', encoding='utf8') as arquivo:
    biblioteca = json.load(arquivo)

carro1 = exercicio_a.Carro(**biblioteca)
print (carro1.modelo)

