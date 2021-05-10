import PySimpleGUI as sg

class TelaAdmin():

    def __init__(self):
        self.__window = None

    def menu_principal(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.ReadButton('Cadastrar Crítico')],
        [sg.ReadButton('Voltar', size=(6,1))]
        ]
        window = sg.Window('Menu Admin', element_justification='c', default_button_element_size=(16, 4), auto_size_buttons=False, grab_anywhere=False, size=(150, 125)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def login(self):
        layout = [
        [sg.Text('Login do usuário Admin')],
        [sg.Text('Senha:', size=(15, 1)), sg.InputText(password_char='*')],
        [sg.ReadButton('Acessar'), sg.ReadButton('Cancelar')],
        ]
        window = sg.Window('Login Admin').Layout(layout)
        senha = window.Read()
        window.Close()
        if senha[0] == 'Acessar':
            return senha[1][0]
        else:
            return None

    def aviso(self, tipo):
        if tipo == 1:
            sg.popup('Senha incorreta!')