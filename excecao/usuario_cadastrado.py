import PySimpleGUI as sg

class UsuarioCadastrado(Exception):
    def __init__(self, usuario):
        sg.popup('ERRO!','{} já cadastrado!'.format(usuario))