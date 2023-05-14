import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver =  conftest.driver
        self.username_field = (By.ID,"username")
        self.password_field = (By.ID,"password")
        self.login_button =   (By.ID,"submit")
        self.error_message_login = (By.ID,"error")

    def fazer_login(self, usuario,senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_mensagem_erro_login_existe(self):   
        self.verificar_se_elemento_existe(self.error_message_login)
    
    def verificar_texto_mensagem_senha_invalida(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f" O text encontrado foi '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'."

    def verificar_mensagem_senha_invalida(self):
        self.verificar_se_elemento_existe(self.mensagem_senha_invalida)

    def verificar_mensagem_usuario_invalido(self):
        self.verificar_se_elemento_existe(self.mensagem_usuario_invalido)