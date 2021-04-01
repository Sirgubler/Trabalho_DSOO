from controle.controlador_autor import ControladorAutor

class TelaAutor:
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("-------- AUTORES --------")
        print("Escolha a opcao")
        print("1 - Incluir Autor")
        print("2 - Listar Autores")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_autor(self):
        print("-------- INCLUIR AUTOR ----------")
        nome = input("Nome: ")

        return {"nome": nome}

    def mostra_autor(self, dados_autor):
        print("NOME DO AUTOR: ", dados_autor["nome"])