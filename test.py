Quando falamos de Desenvolvimento Orientado a Testes a ideia é, na medida do possível, que você crie o teste que irá validar o código a ser criado antes de construir o código de fato.

No nosso caso iremos usar um módulo chamado unittest que é nativo. A lógica aqui é criar uma aplicação hello world com Flash para ser possível expor ela via HTTP e nosso teste basicamente tem que validar retorno 200 (O código HTTP 200 OK é a resposta de status de sucesso que indica que a requisição foi bem sucedida. ) e se o conteúdo da página é o que a gente esperava que fosse.

1- Vamos criar um arquivo chamado test.py

`vim test.py`

```
# -*- coding: utf-8 -*-                                                                                                                                                                                  
from app import app                                                                                                                                                                                      
import unittest                                                                                                                                                                                          
                                                                                                                                                                                                         
class Test(unittest.TestCase):                                                                                                                                                                           
                                                                                                                                                                                                         
    def setUp(self):                                                                                                                                                                                     
        # cria uma instância do unittest, precisa do nome "setUp"                                                                                                                                        
        self.app = app.test_client()                                                                                                                                                                     
                                                                                                                                                                                                         
        # envia uma requisicao GET para a URL                                                                                                                                                            
        self.result = self.app.get('/')                                                                                                                                                                  
                                                                                                                                                                                                         
    def test_requisicao(self):                                                                                                                                                                           
        # compara o status da requisicao (precisa ser igual a 200)                                                                                                                                       
        self.assertEqual(self.result.status_code, 200)                                                                                                                                                   
                                                                                                                                                                                                         
    def test_conteudo(self):                                                                                                                                                                             
        # verifica o retorno do conteudo da pagina                                                                                                                                                       
        self.assertEqual(self.result.data.decode('utf-8'), "Hello World")                                                                                                                                
                                                                                                                                                                                                         
if __name__ == "__main__":                                                                                                                                                                               
    print ('INICIANDO OS TESTES')                                                                                                                                                                        
    print('----------------------------------------------------------------------')                                                                                                                      
    unittest.main(verbosity=2)

```

2- Agora vamos criar o arquivo que iremos codar nossa app.py vazio mesmo para fazer uma validação inicial do nosso teste unitário e na sequência rodar o unittest para testar o código localmente:

`touch app.py`

`python -m unittest -v test`

`py.test test.py`

Veja que ele vai falhar porque nem encontra as referências corretas no arquivo app.py. Super natural até porque ainda não criamos a APP de fato. 
