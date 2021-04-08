class TelaPrincipal:

    def __init__(self):
        pass

    def tela_principal(self):
        print("-------- BEM VINDO AO KOOBS --------")
        print("Rede social para Criticos e Leitores")
        print("1 - Cadastrar")
        print("2 - Entrar")
        print("3 - Visitar")
        print("0 - Sair")
        try:
            opcao_escolhida = int(input("Seleciona uma das opcoes disponiveis: "))
            return opcao_escolhida
        except Exception:
            print("Opcao invalida!")

    def cadastra(self):
        print("-------- BEM VINDO AO KOOBS --------")
        print("--------- MENU DE CADASTRO ---------")
        print("1 - Sign up")
        print("0 - Retornar")
        try:
            opcao_escolhida = int(input("Seleciona uma das opcoes disponiveis: "))
            return opcao_escolhida
        except Exception:
            print("Opcao invalida!\nTente novamente!")
    
    def signupa(self):
        print("-------- BEM VINDO AO KOOBS --------")
        print("Caso deseje fazer um novo cadastro seleciona uma das opcoes\nCaso contrario selecione retornar")
        print("Voce é um Critico ou Leitor?")
        print("1 - Critico")
        print("2 - Leitor")
        print("0 - Retornar ao Menu Principal")
        try:
            opcao_escolhida = int(input("Seleciona uma das opcoes disponiveis: "))
            return opcao_escolhida
        except Exception:
            print("Opcao invalida!\nTente novamente!")

    def entra(self):
        print("1 - Login")
        print("0 - Voltar")
        try:
            opcao_escolhida = int(input("Seleciona uma das opcoes disponiveis: "))
            return opcao_escolhida
        except Exception:
            print("Opcao invalida!")

    def loga_nome(self):
        try:
            login = str(input("Digite o Login do Usuario: "))
            return login
        except Exception:
            print("Erro\nDados inseridos sao invalidos para a busca por um Login!\nTente novamente!")

    def loga_senha(self):
        try:
            senha = str(input("Digite a Senha do Usuario: "))
            return senha
        except Exception:
            print("Erro!\nDados inseridos sao invalidos para a busca por uma senha!\nTente novamente!")

    def erro_logar(self):
        print("Erro!\nAs informacoes inseridas nao estao corretas!")

    def aviso_erro(self):
        print("Erro\nDados inseridos sao invalidos para prosseguir!")