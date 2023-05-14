import pytest
import time
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_LoginSenhaInvalida(self):
        mensagem_erro_esperada = "Your password is invalid!"
        #Instancia os objetos a serem usados no teste
        login_page = LoginPage()

        # Realizando login com senha invãlida
        login_page.fazer_login("student","Password")

        # Verifica se o login nao foi realizado e a mensagem de senha invãlida  é retornada
        time.sleep(1)
        login_page.verificar_mensagem_erro_login_existe()
        
        # Verifica o texto da mensagem de erro
        login_page.verificar_texto_mensagem_senha_invalida(mensagem_erro_esperada)