# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/home', 'r1chuck', 'Área de trabalho')

print(os.path.exists(caminho))

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    if not os.path.isdir(caminho_completo):
        continue
    print(pasta)

    for arquivos in os.listdir(caminho_completo):
        print('  ', arquivos)
