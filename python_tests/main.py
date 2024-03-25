# https://docs.python.org/pt-br/3/library/doctest.html
# https://docs.python.org/pt-br/3/library/unittest.html
from calculadora import soma

try:
    print(soma('15', 15))
except AssertionError as e:
    print(f'conta invalida: {e}')

print('soma ', soma(25, 25))
