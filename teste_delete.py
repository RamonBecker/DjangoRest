import requests

headers = {'Authorization': 'Token 7660b0b2be8f5cefe5f82701333a84aa8417f921'}

url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}5/', headers=headers)

resultado_busca = requests.get(url=url_base_cursos, headers=headers)

print(resultado_busca.json())
# Testando o codigo HTTP

assert resultado.status_code == 204


#print(resultado.text)
# Testando se o tamanho do conteudo retornado é zero

assert len(resultado.text) == 0

