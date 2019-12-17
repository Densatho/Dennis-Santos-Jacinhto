from tkinter import *
from FBase import *
from Hab import *
import Menu_Inicial


class NovoPersonagem:

    def __init__(self, im, idioma,  app, fontpadrao, p):

        self.app = app
        self.idioma = idioma
        self.im = im
        self.fontPadrao = fontpadrao
        self.p = p

        x = {'EN': "Nickname:", 'PT': 'Apelido'}[self.idioma]
        self.nomet = self.im.create_text(510, 20, text=x, anchor=W, font=self.fontPadrao)

        self.nomea = Entry(width=30, font=self.fontPadrao)
        self.nome = self.im.create_window(580, 20, window=self.nomea, anchor=W)

        x = {'PT': "Avançar", 'EN': 'Next'}[self.idioma]
        avancar = Button(text=x, font=self.fontPadrao, width=20, command=self.escolhaclasse)
        self.avancar = self.im.create_window(580, 50, window=avancar, anchor=W)

        x = {'PT': "Voltar", 'EN': 'Back'}[self.idioma]
        volta = Button(text=x, font=self.fontPadrao, width=20,
                       command=self.inicio)
        self.volta = self.im.create_window(580, 80, window=volta, anchor=W)

        self.info = 0
        self.corrigir = 0
        self.avancab = 0

    def escolhaclasse(self):
        
        self.p = [str(self.nomea.get())]
        
        if len(self.p[0]) < 3:
            
            self.im.delete(self.info, self.nomet, self.nome, self.avancar, self.volta)

            x = {'PT': "Nome Invalido", 'EN': 'Invalid Name'}[self.idioma]
            self.info = self.im.create_text(615, 15, text=x, anchor=W, font=self.fontPadrao)

            x = {'PT': "Voltar", 'EN': 'Back'}[self.idioma]
            corrigir = Button(text=x, font=self.fontPadrao, width=20,
                              command=self.np)
            self.corrigir = self.im.create_window(580, 40, window=corrigir, anchor=W)
            
        else:
            
            self.im.delete(self.info, self.nomet, self.nome, self.avancar, self.volta)

            x = {'PT': "Nome Valido", 'EN': 'Valid Name'}[self.idioma]
            self.info = self.im.create_text(625, 15, text=x, anchor=W, font=self.fontPadrao)

            x = {'PT': "Avançar", 'EN': 'Next'}[self.idioma]
            avancab = Button(text=x, font=self.fontPadrao, width=20, command=self.avanca)
            self.avancab = self.im.create_window(580, 40, window=avancab, anchor=W)

    def np(self):

        self.im.delete(self.info, self.corrigir)
        NovoPersonagem(self.im, self.idioma, self.app, self.fontPadrao, self.p)

    def inicio(self):

        self.im.delete(self.info, self.nomet, self.nome, self.avancar, self.volta)
        Menu_Inicial.Inicio(self.im, self.idioma, self.app, self.fontPadrao)

    def avanca(self):

        self.im.delete(self.info, self.avancab)
        
        self.p.append(Player())
        self.p.append([1, 100])
        self.p.append(0)
        self.p.append(25)
        self.p.append([])
        self.p.append(0)

        Habilidades(self.im, self.idioma, self.app, self.fontPadrao, self.p, True, 1)
