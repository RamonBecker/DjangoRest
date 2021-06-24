import requests

#GET Avaliações

#avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/1')

#Acessando o código de status HTTP
#print(avaliacoes.status_code)

#Acessando os dados da resposta

#print(avaliacoes.json())

#print(type(avaliacoes.json()))

#Acessando a quantidade de registros

#print(avaliacoes.json()['count'])

#Acessando a proxima página de resultados

#print(avaliacoes.json()['next'])

#Acessando os resultados desta página

#print(avaliacoes.json()['results'])

#Acessando o primeiro elemento da lista de resultados

#print(avaliacoes.json()['results'][0])

#Acessando o último elemento da lista de resultados

#print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da pessoa que fez a última avaliação

#print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliação

#avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/2')

#print(avaliacao.json())

#GET Cursos

headers = {'Authorization': 'Token 7660b0b2be8f5cefe5f82701333a84aa8417f921'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos', headers=headers)

print(cursos.status_code)

print(cursos.json())