from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class TreinamentoPage(BasePage):
    BOTAO_CLICK_ME = (By.CSS_SELECTOR, '#buttonSimple')
    CAMPO_NOME = (By.CSS_SELECTOR, '#formNome')
    CAMPO_SOBRENOME = (By.CSS_SELECTOR, '#formSobrenome')
    RADIO_SEXO = (By.CSS_SELECTOR, '#formSexoMasc')
    CHECKBOX_COMIDA = (By.CSS_SELECTOR, '#formComidaPizza')
    SELECT_ESCOLARIDADE = (By.CSS_SELECTOR, '#formEscolaridade option[value="superior"]')
    SELECT_ESPORTE = (By.CSS_SELECTOR, '#formEsportes option[value="nada"')
    CAMPO_SUGESTOES = (By.CSS_SELECTOR, '#elementosForm\\:sugestoes')
    TEXTO_RESULTADO = (By.CSS_SELECTOR, '#resultado > span')
    BOTAO_CADASTRAR = (By.CSS_SELECTOR, "#formCadastrar")


    def clicar_botao_click_me(self):
        botao_click_me = self.find_element(*self.BOTAO_CLICK_ME)
        texto_botao_antes = self.get_element_text(botao_click_me)
        assert texto_botao_antes == "Clique Me!"
        botao_click_me.click()

    def recuperar_texto_botao_click_me(self):
        #self.find_element(*self.BOTAO_CLICK_ME)
        return self.get_element_text(self.find_element(*self.BOTAO_CLICK_ME))
    
    def preencher_campo_nome(self, valor):
        campo_nome = self.find_element(*self.CAMPO_NOME)
        campo_nome.send_keys(valor)
    
    def clicar_botao_cadastrar(self):
        self.find_element(*self.BOTAO_CADASTRAR).click()

    def recuperar_texto_alert(self):
        texto_alert = self.get_alert_text()
        return str(texto_alert)
    
    def cadastro(self):
        campo_nome = self.find_element(*self.CAMPO_NOME)
        campo_sobrenome = self.find_element(*self.CAMPO_SOBRENOME)
        campo_sexo = self.find_element(*self.RADIO_SEXO)
        campo_comida = self.find_element(*self.CHECKBOX_COMIDA)
        campo_escolaridade = self.find_element(*self.SELECT_ESCOLARIDADE)
        campo_esporte = self.find_element(*self.SELECT_ESPORTE)
        campo_sugestao = self.find_element(*self.CAMPO_SUGESTOES)

        campo_nome.send_keys("Frederico")
        campo_sobrenome.send_keys("Favaro")
        campo_sexo.click()
        campo_comida.click()
        campo_escolaridade.click()
        campo_esporte.click()
        campo_sugestao.send_keys("Testando campo sugestões")

    def recuperar_texto_resultado(self):
        texto = self.find_element(*self.TEXTO_RESULTADO).text
        return texto

        


