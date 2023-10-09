import requests
from get_token import token

url = 'http://127.0.0.1:3001/alunos'
aluno_data = {
	"nome": "joao",
	"sobrenome": "karisto",
	"email": "joao@email.com",
	"idade": "50",
	"peso": "80.04",
	"altura": "1.90"
}

headers = {
     'Authorization': token
}

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
     print('status code: ', response.status_code)
     print(response.reason)
     print(response.json())
else:
     print('status code:', response.status_code)
     print(response.reason)
     print(response.text)