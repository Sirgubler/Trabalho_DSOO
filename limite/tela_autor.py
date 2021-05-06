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

    def altera_autor_livro(self):
        pass


    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')