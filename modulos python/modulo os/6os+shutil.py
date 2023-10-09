# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

home = os.path.expanduser('~')
desktop = os.path.join(home, 'Área de trabalho')
pasta_origem = os.path.join(desktop, 'lixo')
nova_pasta = os.path.join(desktop, 'nova pasta')

os.makedirs(nova_pasta, exist_ok=True)

for root, dirs, files in os.walk(pasta_origem):
    for dir_ in dirs:
        novo_caminho = os.path.join(
            root.replace(pasta_origem, nova_pasta), dir_)
        os.makedirs(novo_caminho, exist_ok=True)
    for file in files:
        caminho_arquivo = os.path.join(root, file)
        novo_caminho = os.path.join(
            root.replace(pasta_origem, nova_pasta), file)

        shutil.copy(caminho_arquivo, novo_caminho)
