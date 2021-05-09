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
        window = sg.Window('Menu Autor', element_justification='c', default_button_element_size=(16, 4), auto_size_buttons=False, grab_anywhere=False, size=(800, 160)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def altera_genero_livro(self):
        layout = [
        [sg.Text('Digite o nome do Genero: ', size=(20, 1)), sg.InputText(key = 'genero')],
        [sg.Button('Alterar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Alteracao de Genero do Livro').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Alterar':
            return dados_tela['genero']
        else:
            return None
    
    def cadastra_genero(self):
        layout = [
        [sg.Text('Digite o nome do Genero: ', size=(20, 1)), sg.InputText(key = 'genero')],
        [sg.Button('Cadastrar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Cadastrando um novo Genero').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Cadastrar':
            return dados_tela['genero']
        else:
            return None

    def altera_genero(self):
        layout = [
        [sg.Text('Digite o nome do Genero: ', size=(20, 1)), sg.InputText(key = 'genero')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Buscar Genero para Alteracao').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Pesquisar':
            return dados_tela['genero']
        else:
            return None

    def alteracao(self):
        layout = [
        [sg.Text('Digite o novo nome do Genero: ', size=(20, 1)), sg.InputText(key = 'genero')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Alteracao de Genero').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Pesquisar':
            return dados_tela['genero']
        else:
            return None

    def lista_generos(self, generos):
        if generos != []:
            layout = [
                ]
            for genero in generos:
                layout.append([sg.Text('Genero de nome: {}'.format(genero), size=(20, 1))])
            layout.append([sg.Button('Voltar', size=(6,1))])
            window = sg.Window('Lista de Generos').Layout(layout)
            button = window.Read()
            window.Close()
            return button[0]

    def mostra_genero(self, dados_genero):
        print(dados_genero['nome'])

    def remove_genero(self):
        layout = [
        [sg.Text('Digite o nome do Genero: ', size=(20, 1)), sg.InputText(key = 'genero')],
        [sg.Button('Remover'), sg.Button('Cancelar')],
        ]
        window = sg.Window('Deletando Genero').Layout(layout)
        botao, dados_tela = window.Read()
        window.Close()
        if botao == 'Remover':
            return dados_tela['genero']
        else:
            return None  

    def pesquisa_generos(self):
        layout = [
        [sg.Button('Pesquisar Livros do Genero'), sg.ReadButton('Pesquisar Autores do Genero')],
        [sg.Button('Voltar')],
        ]
        window = sg.Window('Menu de Pesquisar Genero').Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def aviso_erro(self):
        print('ERRO!\nDigite um valor válido!')