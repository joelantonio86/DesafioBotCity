import pytest
import time
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_LoginUsuarioInvalido(self):
       mensagem_erro_esperada = "Your username is invalid!"
       #Instancia os objetos a serem usados no teste
       login_page = LoginPage()

       # Fazendo login com a usuario inválido
       login_page.fazer_login("teacher","Password123")

       # Verifica se o login nao foi realizado e a mensagem de usuário invãlido  é retornada
       time.sleep(1)
       login_page.verificar_mensagem_erro_login_existe()
       
       # Verifica o texto da mensagem de erro
       login_page.verificar_texto_mensagem_senha_invalida(mensagem_erro_esperada)