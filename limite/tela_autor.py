import PySimpleGUI as sg

class TelaAutor:
    
    def __init__(self):
        pass
    
    def menu_autor(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.Button('Cadastrar Autor'), sg.Button('Alterar Autor'), sg.Button('Listar Autores'), sg.Button('Remover Autor'), sg.Button('Pesquisar Autores'), ],
        [sg.Button('Voltar', size=(6,1))]
        ]
        window = sg.Window('Menu Autor', element_justification='c', default_button_element_size=(16, 4), auto_size_buttons=False, grab_anywhere=False, size=(1280, 160)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def lista_autores(self, autores):
        if autores != []:
            layout = [
                ]
            for autor in autores:
                layout.append([sg.Button(autor, size=(15, 1))])
            layout.append([sg.Button('Voltar', size=(6,1))])
            window = sg.Window('Lista de Autores').Layout(layout)
            button = window.Read()
            window.Close()
            return button[0]

    def altera_autor_livro(self):
        layout = [
        [sg.Text('Digite o nome do Autor: ', size=(15, 1)), sg.InputText(key = 'autor')],
        [sg.Button('Alterar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Alteracao de Autor do Livro').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Alterar':
            return dados_tela['autor']
        else:
            return None

    def mostra_autor(self, dados_autor):
        print(dados_autor['nome'])

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')