import PySimpleGUI as sg

class Impressoes(Exception):
    def __init__(self, obj):
        if obj == 'Critico':
            sg.popup('Nenhuma Análise Cadastrada!')
        if obj == 'Leitor':
            sg.popup('Nenhuma Nota Cadastrada!')