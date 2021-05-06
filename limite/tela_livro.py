import PySimpleGUI as sg

class TelaLivro():

    def __init__(self):
        pass

    def menu_livro(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.Button('Cadastrar Livro'), sg.Button('Alterar Livro'), sg.Button('Listar Livros'), sg.Button('Remover Livro'), sg.Button('Pesquisar Livros'), sg.Button('Verificar Analises'), sg.Button('Verificar Notas'), sg.Button('Menu Autor'), sg.Button('Menu Genero')],
        [sg.Button('Voltar', size=(6,1))]
        ]
        window = sg.Window('Menu Livro', element_justification='c', default_button_element_size=(16, 4), auto_size_buttons=False, grab_anywhere=False, size=(1340, 160)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]   

    def cadastro_livro(self):
        layout = [
        [sg.Text('Titulo: ', size=(15, 1)), sg.InputText(key = 'titulo')],
        [sg.Text('Autor: ', size=(15, 1)), sg.InputText(key = 'autor')],
        [sg.Text('Genero: ', size=(15, 1)), sg.InputText(key = 'genero')],
        [sg.Button('Criar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Cadastro Livro').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Criar':
            return dados_tela
        else:
            return None
    
    def busca_titulo(self):
        pass

    def altera_livro(self):
        pass

    def altera_titulo(self):
        pass

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')