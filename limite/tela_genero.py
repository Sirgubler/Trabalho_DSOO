class TelaGenero:
    
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- MENU GENEROS --------")
        print("Opcoes disponiveis relacionadas a genero")
        print("1 - Incluir Genero")
        print("2 - Listar Genero")
        print("3 - Excluir Genero")
        print("0 - Retornar")
        try:
            return int(input("Selecione uma opcao : "))
        except Exception:
            print('ERRO!\nDigite apenas números!')

    def pega_nome_genero(self):
        nome = input("DIGITE O NOME DO GENERO: ")

        return nome

    def mostra_genero(self, nome_genero):
        print("EXISTE UM GENERO REGISTRADO DE NOME: ", nome_genero)

    def falha_busca(self):
        print("NAO FORAM ENCONTRADOS REGISTROS!")

    def sucesso_registro(self):
        print("O GENERO FOI REGISTRADO COM SUCESSO!")

    def falha_registro(self):
        print("O GENERO CONSTA NOS REGISTROS!")

    def falha_exclusao(self):
        print("O GENERO NAO CONSTA NOS REGISTROS!")

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')