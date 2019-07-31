from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from busca_google import BuscaGoogle
from selenium import webdriver

class Nucleo():
    def __init__(self):
        self.pesquisa = BuscaGoogle()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def execultar(self):
        self.driver.get(self.pesquisa.link)
        self.google_pais()
        self.abrir_teclado()
        self.digitar_pesquisa()
        self.fechar_teclado()
        self.buscar()
        self.valor_acao()
        self.fechar_navegador()

    def google_pais(self):
        return "Pais: " + str(self.driver.find_element_by_xpath(self.pesquisa.pais_atual).text)

    def abrir_teclado(self):
        while(True):
            try:
                WebDriverWait(self.driver, 1).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, self.pesquisa.teclado_idioma))
                )

                return True
            except:
                print("Aguardando teclado...")
                self.driver.find_element_by_xpath(self.pesquisa.abrir_teclado).click()

    def digitar_pesquisa(self):
        for teclas in self.pesquisa.busca:
            self.driver.find_element_by_xpath(teclas).click()

    def fechar_teclado(self):
        self.driver.find_element_by_xpath(self.pesquisa.fechar_teclado).click()

    def buscar(self):
        self.driver.find_element_by_xpath(self.pesquisa.buscar_botao).submit()

    def valor_acao(self):
        print("R$ " + str(self.driver.find_element_by_xpath(self.pesquisa.valor_acao).text))

    def fechar_navegador(self):
        self.driver.quit()