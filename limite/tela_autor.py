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
                layout.append([sg.Text('Autor de nome: {}'.format(autor), size=(15, 1))])
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
    
    def cadastra_autor(self):
        layout = [
        [sg.Text('Digite o nome do Autor: ', size=(15, 1)), sg.InputText(key = 'autor')],
        [sg.Button('Cadastrar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Cadastrando um novo Autor').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Cadastrar':
            return dados_tela['autor']
        else:
            return None
    
    def altera_autor(self):
        layout = [
        [sg.Text('Digite o nome do Autor: ', size=(15, 1)), sg.InputText(key = 'autor')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Buscar Autor para Alteracao').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Pesquisar':
            return dados_tela['autor']
        else:
            return None

    def alteracao(self):
        layout = [
        [sg.Text('Digite o novo nome do Autor: ', size=(15, 1)), sg.InputText(key = 'autor')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Alteracao de Autor').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Pesquisar':
            return dados_tela['autor']
        else:
            return None

    def mostra_autor(self, dados_autor):
        print(dados_autor['nome'])

    def pesquisa_autores(self):
        layout = [
        [sg.Button('Pesquisar Livros do Autor'), sg.ReadButton('Pesquisar Generos do Autor')],
        [sg.Button('Voltar')],
        ]
        window = sg.Window('Menu de Pesquisar Autor').Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def remove_autor(self):
        layout = [
        [sg.Text('Digite o nome do Autor: ', size=(15, 1)), sg.InputText(key = 'autor')],
        [sg.Button('Remover'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Deletando Autor').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Remover':
            return dados_tela['autor']
        else:
            return None  

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')