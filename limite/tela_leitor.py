import PySimpleGUI as sg

class TelaLeitor():

    def __init__(self):
        pass

    #Opções gerais da classe Leitor. É chamada pela função abrir_tela_leitor() 
    def menu_principal(self):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.ReadButton('Login'), sg.ReadButton('Cadastro')],
        [sg.ReadButton('Voltar', size=(6,1))]
        ]
        window = sg.Window('Menu Leitor', element_justification='c', default_button_element_size=(16, 4), auto_size_buttons=False, grab_anywhere=False, size=(400, 125)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def selecao_de_leitor(self):
        layout = [
        [sg.Text('Login', size=(15, 1)), sg.InputText()],
        [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
        [sg.ReadButton('Acessar'), sg.ReadButton('Cancelar')],
        ]
        window = sg.Window('Login Leitor').Layout(layout)
        login = window.Read()
        window.Close()
        if login[0] == 'Acessar':
            return login[1]
        else:
            return None

    def cadastro_de_leitor(self):
        layout = [
        [sg.Text('Digite o nome do leitor que deseja cadastrar')],
        [sg.Text('Nome', size=(15, 1)), sg.InputText(size=(45,1), )],
        [sg.Text('Senha', size=(15, 1)), sg.InputText(password_char='*')],
        [sg.ReadButton('Cadastrar'), sg.ReadButton('Cancelar')],
        ]
        window = sg.Window('Cadastro de Leitor').Layout(layout)
        cadastro = window.Read()
        window.Close()
        if cadastro[0] == 'Cadastrar':
            return cadastro[1]
        else:
            return None

    def inclusao_de_livro_lido(self):
        layout = [
        [sg.Text('Nota:', size=(15, 1))],
        [sg.Combo([10,9,8,7,6,5,4,3,2,1], enable_events=True, key='Nota')]
        ]
        window = sg.Window('Análise', element_justification='c').Layout(layout)
        cadastro = window.Read()
        window.Close()
        self.aviso(5)
        return cadastro[1]['Nota']

    #Opções específicas do leitor. É chamada pela função abrir_menu_leitor()
    def menu_leitor(self, nome):
        sg.ChangeLookAndFeel('DarkGrey3')
        layout = [
        [sg.ReadButton('Ver livros lidos'), sg.ReadButton('Incluir um livro lido')],
        [sg.ReadButton('Voltar', size=(6,1))]
        ]
        window = sg.Window('Leitor: {}'.format(nome), element_justification='c', default_button_element_size=(20, 4), auto_size_buttons=False, grab_anywhere=False, size=(400, 125)).Layout(layout)
        button = window.Read()
        window.Close()
        return button[0]

    def livros_lidos(self, livros_lidos):
        if livros_lidos != {}:
            layout = [
                ]
            for livro in livros_lidos:
                layout.append([sg.Text('{}: {}'.format(livro, livros_lidos[livro]))])
            layout.append([sg.ReadButton('OK', size=(6,1))])
            window = sg.Window('Notas').Layout(layout)
            window.Read()
            window.Close()   
        else:
            self.aviso(4)     
            return

    def aviso(self, tipo):
        if tipo == 1:
            sg.popup('Leitor Cadastrado!')
        elif tipo == 2:
            sg.popup('ERRO!', 'Login inválido')
        elif tipo == 3:
            sg.popup('ERRO!','Leitor já cadastrado!')
        elif tipo == 4:
            sg.popup('Nunhum Livro Lido!')
        elif tipo == 5:
            sg.popup('Livro Lido com Sucesso!')
        elif tipo == 6:
            layout = [
            [sg.Text('Esse livro já possui uma nota, deseja altera-la?')],
            [sg.ReadButton('Sim', size=(6,1)), sg.ReadButton('Não', size=(6,1))]
            ]
            window = sg.Window('Aviso!', element_justification='c', default_button_element_size=(6, 1), auto_size_buttons=False, grab_anywhere=False).Layout(layout)
            button = window.Read()
            window.Close()
            if button[0] == 'Sim':
                return True
            else:
                return False
