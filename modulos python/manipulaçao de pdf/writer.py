from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

pasta_raiz = Path(__file__).parent
pasta_nova = pasta_raiz / 'pdfs_novos'
boletim_focus = pasta_raiz / 'focus.pdf'

pasta_nova.mkdir(exist_ok=True)

reader = PdfReader(boletim_focus)
print(len(reader.pages))

writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

with open(pasta_nova / 'page0.pdf', 'wb') as arquivo:
    writer.write(arquivo)


for i,page in enumerate(reader.pages):
    writer = PdfWriter() 
    writer.add_page(page)

    with open(pasta_nova / f'pages{i}.pdf', 'wb') as arquivo:
        writer.write(arquivo)