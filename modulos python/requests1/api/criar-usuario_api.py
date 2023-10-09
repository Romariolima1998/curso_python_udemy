import requests

url = 'http://127.0.0.1:3001/users'

user_data = {
	"nome": "nome valido",
	"password": "123456",
	"email": "email_valido@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
     print('status code: ', response.status_code)
     print(response.reason)
     print(response.json())
else:
     print('status code:', response.status_code)
     print(response.reason)
     print(response.text)