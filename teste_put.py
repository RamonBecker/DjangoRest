import requests

headers = {'Authorization': 'Token 7660b0b2be8f5cefe5f82701333a84aa8417f921'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo curso de Scrum 3",
    "url" :"http://geekuniversity.com.br/ncs3"
}
# Buscando o curso com id 5

#curso = requests.get(url=f'{url_base_cursos}5/', headers=headers)

#print(curso.json())


resultado = requests.put(url=f'{url_base_cursos}5/', headers=headers, data=curso_atualizado)
#Testando o código de status HTTP

assert resultado.status_code == 200

# Testando o titulo

assert resultado.json()['titulo'] == curso_atualizado['titulo']