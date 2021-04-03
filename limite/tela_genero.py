class TelaGenero:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- AUTORES --------")
        print("Escolha a opcao")
        print("1 - Incluir Genero")
        print("2 - Listar Generos")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_genero(self):
        print("-------- INCLUIR GENERO ----------")
        nome = input("Nome: ")

        return {"nome": nome}

    def mostra_genero(self, dados_genero):
        print("NOME DO GENERO: ", dados_genero["nome"])