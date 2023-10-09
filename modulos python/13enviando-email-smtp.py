import os
from dotenv import load_dotenv
from pathlib import Path
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

# dados do remetente e destinatario
remetente = os.getenv('FROM_EMAIL')
destinatario = remetente

# configuraçoes smtp
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = remetente
smtp_password = os.getenv('FROM_PASSWORD')
print(smtp_password, smtp_username)

# caminho arquivo html
caminho_html = Path(__file__).parent / 'email.html'

with open(caminho_html, 'r') as arquivo:
    print("cheguei aki")
    texto_arquivo = arquivo.read()
    print(texto_arquivo)
    template = Template(texto_arquivo)
    texto_email = template.substitute({'nome': 'joao'})

    print(texto_email)

    mime_multipart = MIMEMultipart()
    mime_multipart['from'] = remetente
    mime_multipart['to'] = destinatario
    mime_multipart['subject'] = 'este e o assunto'

    corpo_do_email = MIMEText(texto_email, 'html', 'utf-8')
    mime_multipart.attach(corpo_do_email)

# envia o email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(mime_multipart)
        print('email enviado com sucesso')
