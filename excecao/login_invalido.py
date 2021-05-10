import PySimpleGUI as sg

class LoginInvalido(Exception):
    def __init__(self):
        sg.popup('ERRO!','Login inválido!')