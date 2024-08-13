Funcionalidade: Treinamento de Automaçao

    @TesteSimples
    Cenário: Interagir com botões
        Dado que a página de treinamento seja acessada
        Quando o botão click me for clicado
        Então o seu valor deverá mudar para "Obrigado!"

    @abc
    Cenário: Verificar que o não é possível cadastrar um registro sem sobrenome
        Dado que a página de treinamento seja acessada
        Quando o valor "Frederico" for inserido no campo Nome
        E o cadastro for efetuado
        Então um alert com a mensagem "Sobrenome eh obrigatorio" deverá aparecer na tela

    @CadastroUsuário
    Cenário: Cadastrar um novo usuário com sucesso
        Dado que a página de treinamento seja acessada
        Quando o usuário preencher os campos
        E o cadastro for efetuado
        Então a mensagem "Cadastrado!" deverá aparecer 
        
