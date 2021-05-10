import PySimpleGUI as sg

class NomeInvalido(Exception):
    def __init__(self, obj):
        if obj == 'Leitor':
            sg.popup('Nome do Leitor incorreto.')
        if obj == 'Critico':
            sg.popup('Nome do Crítico incorreto.')