import requests
import jsonpath

headers = {'Authorization': 'Token 7660b0b2be8f5cefe5f82701333a84aa8417f921'}

cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos', headers=headers)

#avaliacoes = requests.get(url='http://127.0.0.1:8000/api/v2/avaliacoes/', headers=headers)

#resultados = jsonpath.jsonpath(cursos.json(), 'results')
#print(resultados)

#primeiro_resultado = jsonpath.jsonpath(cursos.json(), 'results[0]')

#print(primeiro_resultado)

#titulo = jsonpath.jsonpath(cursos.json(), 'results[0].titulo')

#print(titulo)

#media_avaliacoes = jsonpath.jsonpath(cursos.json(), 'results[0].media_avaliacoes')

#print(media_avaliacoes)


#titulos = jsonpath.jsonpath(cursos.json(), 'results[*].titulo')

#print(titulos)


medias = jsonpath.jsonpath(cursos.json(), 'results[*].media_avaliacoes')

print(medias)
