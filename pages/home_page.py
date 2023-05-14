import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    def __init__(self):
        self.driver = conftest.driver
        self.mensagem_login_sucesso = (By.XPATH, "//h1[@class='post-title' and text()='Logged In Successfully']")
       

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.mensagem_login_sucesso)