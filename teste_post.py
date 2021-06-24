import re
import requests

headers = {'Authorization': 'Token 7660b0b2be8f5cefe5f82701333a84aa8417f921'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Gerencia Ágil de Projetos com Scrum",
    "url": "http://www.geekuniversity.com.br/scrum",   
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)

#Testando o código de status HTTP
assert resultado.status_code == 201

#Testando se o titulo do curso retornado é o mesmo do informado

assert resultado.json()['titulo'] == novo_curso['titulo']

