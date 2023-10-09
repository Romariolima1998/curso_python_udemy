"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
próximo -> me entregue o próximo valor
iter -> me entregou seu iterador
"""
# para letra no texto
texto  =  'Luiz'   # iterável

# iterador = iter(texto) # iterador

# enquanto verdadeiro:
# tentar:
# letra = next(iterador)
# print(letra)
# exceto StopIteration:
# quebrar

for  letra  in  texto :
    print ( letra )