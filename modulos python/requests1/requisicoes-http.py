# Tutorial -> https://youtu.be/Qd8JT0bnJGs

import requests

# http:// porta 80
# https:// porta 443
url = 'http://0.0.0.0:3000'

response = requests.get(url)

print(response.status_code)
# cabeçalho
# print(response.headers)

# conteudo no formato bites
# print( response.content)

# se a resposta for em json
# print(response.json())

# resposta em txt html
print(response.text)