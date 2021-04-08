class TelaCritico:

    def __init__(self):
        pass

    def cadastra_nome(self):
        erroPrimeiroNome = True
        erroSegundoNome = True
        primeiro_nome_efetivado = None
        segundo_nome_efetivado = None
        while erroPrimeiroNome:
            primeiro_nome = input("Digite apenas o seu primeiro nome: ")
            if primeiro_nome.isalpha():
                primeiro_nome_efetivado = primeiro_nome
                erroPrimeiroNome = False
            else:
                print("Erro!\nDigite apenas letras!\nTente novamnete!")
        while erroSegundoNome:
            segundo_nome = input("Digite apenas o seu segundo nome: ")
            if segundo_nome.isalpha():
                segundo_nome_efetivado = segundo_nome
                erroSegundoNome = False
            else:
                print("Erro!\nDigite apenas letras!\nTente novamnete!")
        
        nome = "{} {}".format(primeiro_nome_efetivado, segundo_nome_efetivado)
        return nome

    def cadastra_registro_profissional(self):
        try:
            registro_profissional = int(input("Digite o seu registro profissional: "))
            return registro_profissional
        except Exception:
            print("Erro!\nO registro profissional deve conter apenas numeros!")

    def cadastra_login(self):
        try:
            login = str(input("Digite seu login de usuario: "))
            return login
        except Exception:
            print("Erro!\nA forma como digitou é inviável!\nTente novamente!")

    def cadastra_senha(self):
        try:
            senha = str(input("Digite sua senha: "))
            return senha
        except Exception:
            print("Erro!\nA forma como digitou é inviável!\nTente novamente!")
    
    def sucesso_cadastra(self):
        print("Parabens!\nO cadastro foi um sucesso!")

    def erro_cadastra(self):
        print("Erro!\nInfelizmente ja existe outro usuario com o login escolhido!\nTente novamente posteriormente!")

    def aviso_erro(self):
        pass