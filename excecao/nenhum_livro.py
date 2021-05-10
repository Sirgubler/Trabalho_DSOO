import PySimpleGUI as sg

class NenhumLivro(Exception):
    def __init__(self, obj):
        if obj == 'Leitor':
            sg.popup('Nunhum Livro Lido!')
        elif obj == 'Critico':
            sg.popup('Nunhum Livro Analisado!')
        elif obj == 'Livro':
            sg.popup('Nenhum Livro Cadastrado')