from pathlib import Path
from PyPDF2 import PdfMerger

pasta_raiz = Path(__file__).parent
pasta_nova = pasta_raiz / 'pdfs_novos'
boletim_focus = pasta_raiz / 'focus.pdf'


files = [
    pasta_nova / 'pages0.pdf',
    pasta_nova / 'pages1.pdf'
]
merger = PdfMerger()
for file in files:
    merger.append(file)

with open(pasta_nova / 'marger.pdf', 'wb') as arquivo:
    merger.write(arquivo)