from tkinter import *
from NP import NovoPersonagem
from Load import Load
import Exit


class Inicio:

    def __init__(self, im, idioma, app, fontpadrao):

        self.idioma = idioma
        self.fontPadrao = fontpadrao
        self.p = []
        self.app = app
        self.im = im

        x = {'PT': 'Novo Personagem', 'EN': 'New Character'}[self.idioma]
        new = Button(text=x, font=self.fontPadrao, width=20, command=self.np)
        self.new = self.im.create_window(580, 40, window=new, anchor=W)

        x = {'PT': 'Carregar Personagem', 'EN': 'Load Character'}[self.idioma]
        load = Button(text=x, font=self.fontPadrao,  width=20, command=self.load)
        self.loadb = self.im.create_window(580, 70, window=load, anchor=W)

        x = {'PT': 'Sair', 'EN': 'Exit'}[self.idioma]
        sair = Button(text=x, font=self.fontPadrao, width=20, command=self.sair)
        self.sairb = self.im.create_window(580, 100, window=sair, anchor=W)

    def np(self):
        
        self.im.delete(self.new, self.loadb, self.sairb)
        NovoPersonagem(self.im, self.idioma, self.app, self.fontPadrao, self.p)

    def sair(self):

        Exit.Exit(self.app)

    def load(self):

        self.im.delete(self.new, self.loadb, self.sairb)
        Load(self.im, self.idioma, self.app, self.fontPadrao, self.p, True, False, 1)
