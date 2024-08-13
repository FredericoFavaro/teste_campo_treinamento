from behave import given, when, then
from features.pages.treinamento_page import TreinamentoPage
import time

# region Teste Click Botão
@given(u'que a página de treinamento seja acessada')
def step_impl(context):
    context.driver.get("https://wcaquino.me/cypress/componentes.html")
    context.treinamento_page = TreinamentoPage(context.driver)

@when(u'o botao click me for clicado')
def step_impl(context):
    context.treinamento_page.clicar_botao_click_me()


@then(u'o seu valor deverá mudar para "{texto_correto}"')
def step_impl(context, texto_correto):
    texto_obtido = context.treinamento_page.recuperar_texto_botao_click_me()
    assert texto_obtido == texto_correto, f"O texto obtido '{texto_obtido}' foi diferente do texto esperado '{texto_correto}'"

# endregion

# region Teste Alert Sobrenome Obrigatório
@when(u'o valor "{valor}" for inserido no campo Nome')
def inserir_texto_campo_nome(context, valor):
    context.treinamento_page.preencher_campo_nome(valor)


@when(u'o cadastro for efetuado')
def efeturar_cadastro(context):
    context.treinamento_page.clicar_botao_cadastrar()


@then(u'um alert com a mensagem "{mensagem}" deverá aparecer na tela')
def mensagem_erro_alert_sobrenome(context, mensagem):
    texto_alert = context.treinamento_page.recuperar_texto_alert()
    assert  texto_alert == mensagem, f"Mensagem de erro:\nO texto do alert '{texto_alert}'\n foi diferente do esperado '{mensagem}'"

# endregion

# region teste cadastro
@when(u'o usuário prencher os campos')
def preencher_formulario(context):
    context.treinamento_page.cadastro()

@when(u'o cadastro for efetuado2')
def efeturar_cadastro2(context):
    context.treinamento_page.clicar_botao_cadastrar()

@then(u'a mensagem "{valor}" deverá aparecer')
def texto_resultado(context, valor):
    resultado = context.treinamento_page.recuperar_texto_resultado()
    assert  resultado == valor, f"Mensagem de erro:\nO texto do alert '{resultado}'\n foi diferente do esperado '{valor}'"
    time.sleep(5)
