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
        layout = [
        [sg.Text('Digite o titulo do livro: ', size=(15, 1)), sg.InputText(key = 'titulo')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Buscar Livro para Alteracao').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Pesquisar':
            return dados_tela['titulo']
        else:
            return None

    def altera_livro(self):
        layout = [
        [sg.Button('Alterar Titulo'), sg.ReadButton('Alterar Autor'), sg.ReadButton('Alterar Genero')],
        [sg.Button('Cancelar')],
        ]
        window = sg.Window('Alteracao de Livro Pesquisado').Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]
    
    def altera_titulo(self):
        layout = [
        [sg.Text('Digite o novo titulo do livro: ', size=(15, 1)), sg.InputText(key = 'titulo')],
        [sg.Button('Alterar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Alteracao de Titulo').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Alterar':
            return dados_tela['titulo']
        else:
            return None
    
    def lista_livros(self, livros):
        if livros != []:
            layout = [
                ]
            for livro in livros:
                layout.append([sg.Button(livro, size=(15, 1))])
            layout.append([sg.Button('Voltar', size=(6,1))])
            window = sg.Window('Lista de Livros').Layout(layout)
            button = window.Read()
            window.Close()
            return button[0]

    def mostra_livro(self, dados_livro):
        if dados_livro != {}:
            layout = [
            [sg.Text('Titulo: {}'.format(dados_livro['titulo']), size=(15, 1))],
            [sg.Text('Autor: {}'.format(dados_livro['autor']), size=(15, 1))],
            [sg.Text('Genero: {}'.format(dados_livro['genero']), size=(15, 1))],
            [sg.Button('Voltar')],
            ]
            window = sg.Window('Lista de Livros').Layout(layout)
            button = window.Read()
            window.Close()
            if button == 'Voltar':
                return 'Voltar'  

    def remove_livro(self):
        layout = [
        [sg.Text('Digite o titulo do livro: ', size=(15, 1)), sg.InputText(key = 'titulo')],
        [sg.Button('Remover'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Deletando Livro').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Remover':
            return dados_tela['titulo']
        else:
            return None  

    def aviso_sucesso(self):
        pass

    def aviso_erro(self):
        sg.popup('Erro!')