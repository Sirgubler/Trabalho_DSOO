import PySimpleGUI as sg
from excecao.nenhum_livro import NenhumLivro

class TelaCritico():

    def __init__(self):
        self.__window = None

    #Opções gerais da classe Critico. É chamada pela função abrir_tela_critico()
    def menu_principal(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.ReadButton('Login')],
        [sg.ReadButton('Voltar', size=(6,1))]
        ]
        window = sg.Window('Menu Crítico', element_justification='c', default_button_element_size=(16, 4), auto_size_buttons=False, grab_anywhere=False, size=(150, 125)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def selecao_de_critico(self):
        layout = [
        [sg.Text('Login', size=(15, 1)), sg.InputText()],
        [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
        [sg.ReadButton('Acessar'), sg.ReadButton('Cancelar')],
        ]
        window = sg.Window('Login Crítico').Layout(layout)
        login = window.Read()
        window.Close()
        if login[0] == 'Acessar':
            return login[1]
        else:
            return None

    def cadastro_de_critico(self):
        layout = [
        [sg.Text('Digite o nome do crítico que deseja cadastrar')],
        [sg.Text('Nome', size=(15, 1)), sg.InputText(size=(45,1), )],
        [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
        [sg.ReadButton('Cadastrar'), sg.ReadButton('Cancelar')],
        ]
        window = sg.Window('Cadastro de Crítico').Layout(layout)
        cadastro = window.Read()
        window.Close()
        if cadastro[0] == 'Cadastrar':
            return cadastro[1]
        else:
            return None


    def inclusao_de_livro_analisado(self):
        layout = [
        [sg.Text('Análise:', size=(15, 1)), sg.Multiline(size=(100,5))],
        [sg.ReadButton('Cadastrar'), sg.ReadButton('Cancelar')],
        ]
        window = sg.Window('Análise').Layout(layout)
        cadastro = window.Read()
        window.Close()
        if cadastro[0] == 'Cadastrar':
            self.aviso(2)
            return cadastro[1][0]
        else:
            return None

    #Opções específicas do critico. É chamada pela função abrir_menu_critico()
    def menu_critico(self, nome):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.ReadButton('Ver livros analisados'), sg.ReadButton('Incluir um livro analisado')],
        [sg.ReadButton('Voltar', size=(6,1))]
        ]
        window = sg.Window('Crítico: {}'.format(nome), element_justification='c', default_button_element_size=(20, 4), auto_size_buttons=False, grab_anywhere=False, size=(400, 125)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def livros_analisados(self, livros_analisados):
        if livros_analisados != {}:
            layout = [
                ]
            for livro in livros_analisados:
                layout.append([sg.Text('{}:'.format(livro))])
                layout.append([sg.Text(livros_analisados[livro], size=(100,5))])
            layout.append([sg.ReadButton('OK', size=(6,1))])
            window = sg.Window('Análises').Layout(layout)
            window.Read()
            window.Close()   
        else:
            raise NenhumLivro('Critico')

    def aviso(self, tipo):
        if tipo == 1:
            sg.popup('Crítico Cadastrado!')
        elif tipo == 2:
            sg.popup('Livro Analisado com Sucesso!')
        elif tipo == 3:
            layout = [
            [sg.Text('Esse livro já possui uma análise, deseja altera-la?')],
            [sg.ReadButton('Sim', size=(6,1)), sg.ReadButton('Não', size=(6,1))]
            ]
            window = sg.Window('Aviso!', element_justification='c', default_button_element_size=(6, 1), auto_size_buttons=False, grab_anywhere=False).Layout(layout)
            button = window.Read()
            window.Close()
            if button[0] == 'Sim':
                return True
            else:
                return False
            
