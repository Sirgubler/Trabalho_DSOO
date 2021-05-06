import PySimpleGUI as sg

class TelaGenero:
    
    def __init__(self):
        pass

    def menu_genero(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.Button('Cadastrar Genero'), sg.Button('Alterar Genero'), sg.Button('Listar Generos'), sg.Button('Remover Genero'), sg.Button('Pesquisar Generos'), ],
        [sg.Button('Voltar', size=(6,1))]
        ]
        window = sg.Window('Menu Autor', element_justification='c', default_button_element_size=(16, 4), auto_size_buttons=False, grab_anywhere=False, size=(1280, 160)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

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