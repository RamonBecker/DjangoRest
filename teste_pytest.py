import requests


class TestCurso:
    headers = {'Authorization': 'Token 7660b0b2be8f5cefe5f82701333a84aa8417f921'}
    
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_base_cursos, headers=self.headers)
        
        assert resposta.status_code == 200
        
    
    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_cursos}1/', headers=self.headers)
        
        assert resposta.status_code == 200
        
    def test_post_curso(self):
        novo_curso = {
            "titulo": "Curso de Programação com Ruby",
            "url": "http://www.geekuniversity.com.br/ruby"
        }
        
        resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo_curso)
        
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo_curso['titulo']
        
    def test_curso_put(self):
        atualizado_curso = {
            "titulo": "Novo curso de Ruby",
            "url": "http://www.geekuniversity.com.br/novoruby"
        }
        
        
        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado_curso)
        
        assert resposta.status_code == 200
    
    def test_put_titulo_curso(self):
        atualizado_curso = {
            "titulo": "Novo curso de Ruby 2",
            "url": "http://www.geekuniversity.com.br/ncr2"
        }        
        
        resposta = requests.put(url=f'{self.url_base_cursos}2/', headers=self.headers, data=atualizado_curso)
        
        
        assert resposta.json()['titulo'] == atualizado_curso['titulo']
        
    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_cursos}2/', headers=self.headers)
        
        assert resposta.status_code == 204 and len(resposta.text) == 0