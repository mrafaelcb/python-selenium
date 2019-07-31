#coding: utf-8

class BuscaGoogle():
    def __init__(self, link = "https://www.google.com.br/"):
        self.link = link
        self.pais_atual = "/html/body/div[1]/div[7]/div[1]/div/div/div/div/div/div/span"
        self.buscar_entrada = "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div/div[1]/input"
        self.buscar_botao = "/html/body/div[1]/div[3]/form/div[2]/div/div[2]/div[2]/div[2]/center/input[1]"
        self.abrir_teclado = "/html/body/div[1]/div[3]/form/div[2]/div/div[1]/div/div[2]/div[1]/span"
        self.fechar_teclado = "/html/body/div[3]/div[1]/div[2]/div/div"
        self.teclado_idioma = "/html/body/div[3]/div[1]/div[1]"
        self.valor_acao = "/html/body/div[7]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/g-card-section/div/g-card-section/div[2]/span[1]/span/span[1]"
        self.busca = [
            "/html/body/div[3]/div[2]/div[4]/button[1]/span",
            "//*[@id=\"K79\"]",
            "/html/body/div[3]/div[2]/div[2]/button[9]/span",
            "/html/body/div[3]/div[2]/div[4]/button[7]/span",
            "//*[@id=\"K82\"]",
            "//*[@id=\"K52\"]"
        ]