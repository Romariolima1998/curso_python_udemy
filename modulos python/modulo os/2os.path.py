# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
# /home/r1chuck/Área de trabalho/nova
import os

# junta os nomes das pastas
caminho = os.path.join(
    '/', 'home', 'r1chuck', 'Área de trabalho', 'nova', 'arquivo.txt')
print(caminho)

# separa o diretorio do arquivo
diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)

# separa o diretorio e o nome do arquivo da extencao
diretorio1, extecao = os.path.splitext(caminho)
print(diretorio)
print(extecao)

# verifica se a pasta exite
print(os.path.exists(diretorio))

# pasta absoluta visual code
print(os.path.abspath('.'))

# parte final do caminho
print(os.path.basename(caminho))

# nome das patas
print(os.path.dirname(caminho))
