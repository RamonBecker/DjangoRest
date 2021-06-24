import requests

headers = {'Authorization': 'Token 7660b0b2be8f5cefe5f82701333a84aa8417f921'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

#Testando se o endpoint esta correto    
assert resultado.status_code == 200

#Testando a quantidade de registros
assert resultado.json()['count'] == 6

#print(resultado.json())

#Testando se o titulo do primeiro curso esta correto

assert resultado.json()['results'][0]['titulo'] == 'Criacao de Apis REst com Django Rest framewok'