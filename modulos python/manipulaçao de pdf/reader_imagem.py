# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader

pasta_raiz = Path(__file__).parent
pasta_nova = pasta_raiz / 'pdfs_novos'
boletim_focus = pasta_raiz / 'focus.pdf'

pasta_nova.mkdir(exist_ok=True)

reader = PdfReader(boletim_focus)
print(len(reader.pages))

# for page in reader.pages:
#   print(page)

page0 = reader.pages[0]
print(page0.extract_text())

image = page0.images[0]
print(image)

with open(pasta_nova / image.name, 'wb') as arquivo:
    arquivo.write(image.data)
