class TelaAutor:
    
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- MENU AUTORES --------")
        print("Opcoes disponiveis relacionadas a autor")
        print("1 - Incluir Autor")
        print("2 - Listar Autores")
        print("3 - Excluir Autor")
        print("0 - Retornar")
        try:
            return int(input("Selecione uma opcao : "))
        except Exception:
            print('ERRO!\nDigite apenas números!')

    def pega_nome_autor(self):
        nome = input("DIGITE O NOME DO AUTOR: ")

        return nome

    def mostra_autor(self, nome_autor):
        print("EXISTE UM AUTOR REGISTRADO DE NOME: ", nome_autor)

    def falha_busca(self):
        print("NAO FORAM ENCONTRADOS REGISTROS!")

    def sucesso_registro(self):
        print("O AUTOR FOI REGISTRADO COM SUCESSO!")

    def falha_registro(self):
        print("O AUTOR JA ESTA REGISTRADO!")

    def falha_exclusao(self):
        print("O AUTOR NAO CONSTA NOS REGISTROS!")

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')