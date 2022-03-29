import random
import os
import site
import PySimpleGUI as sg
from numpy import size
import string

class passgen():
    def __init__(self):
        sg.theme('black')
        layout=[ 
                [
                    sg.Text('site/software',size=(10,1)),
                    sg.Input(key="site",size=(20,1))
                ],
                [
                    sg.Text('e-mail/usuario',size=(10,1)),
                    sg.Input(key="user",size=(20,1))
                ], 
                [
                    sg.Text('quantidades de caracteres',size=(10,1)),
                    sg.Combo(key='total_chars',values=list(range(31)),default_value=1,size=(3,1))
                ],
                [sg.Output(size=(32,5))],
                [sg.Button('gerar senha')]
        ]
        #declarar layout
        self.janela= sg.Window('pass generetor',layout)

    def iniciar(self):
        while True:

            event,valores = self.janela.read()
            
            if event ==sg.WINDOW_CLOSED:
                break
            
            if event == 'gerar senha':
                new_password = self.GenPassword(int(valores['total_chars']))
                self.salvar(valores,new_password)
                print(new_password)

    def GenPassword(self,len_pass):
        ascii_option = string.ascii_letters
        number_options = string.digits
        punt_options = string.punctuation

        options  = ascii_option + number_options + punt_options

        password=""
        for numero_digitos in range(len_pass):
            password+= random.choice(options)

        return password


    def salvar(self,valores,newpassword):
        with open('criador_de_senha/senhas.txt','a',newline="") as arquivo:
            arquivo.write("site:{},usuario{},senha{}\n".format(valores["site"],valores["user"],newpassword))



simulacao= passgen()
simulacao.iniciar()