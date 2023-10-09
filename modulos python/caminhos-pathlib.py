from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

print(caminho_arquivo.parent)

nova_pasta = caminho_arquivo.parent / 'nova pasta'
nova_pasta.mkdir(exist_ok=True)

print(Path.home())

# para criar um arquivo

arquivo = Path.home() / 'arquivo.txt'
arquivo.touch()
arquivo.write_text('ola mundo')
print(arquivo.read_text())
# para apagar
arquivo.unlink()

with arquivo.open('a+') as file:
    file.write('primeira lina \n')
    file.write('segunda linha')

print(arquivo.read_text())

pasta_arquivo = Path.home() / 'Área de trabalho' / 'nova pasta'
pasta_arquivo.mkdir(exist_ok=True)

for i in range(10):
    file = pasta_arquivo / f'arquivo{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch

    with file.open('a+') as text_file:
        text_file.write('hello word \n')
        text_file.write(f'file{i}')
