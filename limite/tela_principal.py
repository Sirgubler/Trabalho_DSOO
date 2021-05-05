import PySimpleGUI as sg

class TelaPrincipal():

    def __init__(self):
        self.__window = None


    #Opções gerais da classe ControladorPrincipal. É chamada pela função abrir_tela()
    def menu_principal(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.ReadButton('Menu Livros'), sg.ReadButton('Menu Usuários')],
        [sg.ReadButton('Sair', size=(6,1))]
        ]
        window = sg.Window('Menu Principal', element_justification='c', default_button_element_size=(12, 4), auto_size_buttons=False, grab_anywhere=False, size=(300, 125)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    #Opções de seleção de usuário. É chamada pela função abrir_tela_usuario()
    def menu_usuario(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.ReadButton('Menu Leitor'), sg.ReadButton('Menu Crítico'), sg.ReadButton('Menu Admin')],
        [sg.ReadButton('Voltar', size=(6,1))]
        ]
        window = sg.Window('Menu Usuários', element_justification='c', default_button_element_size=(12, 4), auto_size_buttons=False, grab_anywhere=False, size=(400, 125)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]
