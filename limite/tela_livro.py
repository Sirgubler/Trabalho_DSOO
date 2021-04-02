from controle.controlador_livro import ControladorLivro

class TelaLivro():
    def __init__(self):
        pass

    def tela_opcoes(self):
        print("----------   LIVROS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Livro")
        print("2 - Remover Livro")
        print("3 - Listar Livros")
        print("4 - Pesquisar Livro por Titulo")
        print("5 - Ver Analises")
        print("6 - Nota")
        print("0 - Retornar")

        opcao = int(input("Selecione a opção desejada: "))
        return opcao

    def pega_dados_livro(self):
        print("-------- INCLUIR LIVRO ----------")
        nome = input("Nome: ")
        autor = input("Autor: ")
        genero = input("Genero: ")

        return {"nome": nome, "autor": autor, "genero": genero}
    
    def cadastro_livro(self):
        pass

    def exclusao_livro(self):
        print("-------- EXCLUIR LIVRO --------")


    def cadastro_leitor(self):
        pass

    def pesquisa_leitor(self):
        pass

    def analises(self):
        pass