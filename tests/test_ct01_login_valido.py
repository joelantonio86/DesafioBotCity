import pytest
import conftest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestCT01:
    def test_ct01_LoginValido(self):
        #Instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage ()

        # Fazendo login de sucesso
        login_page.fazer_login("student","Password123")
        
        # Verifica se o login foi realizado com sucesso
        home_page.verificar_login_com_sucesso()
        


