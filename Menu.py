from tkinter import *
from Mapa import Mapa
from Status import Status
from Save import Save
from Load import Load
from Config import OP
from Exit import Exit


class Menu:

    def __init__(self, im, idioma, app, fontpadrao, p, mp):

        im.destroy()
        self.im = Canvas(app, width=2000, height=1100)
        imagem = PhotoImage(file="img\\1.png")
        painel = self.im.create_image(0, 0, image=imagem, anchor=NW)
        self.im.lower(painel)
        self.im.pack()
        self.im.image = imagem

        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp

        x = {'PT': 'Mapa', 'EN': 'Map'}[self.idioma]
        mapa = Button(text=x, font=self.fontPadrao, width=20, command=self.mapa)
        self.mapab = self.im.create_window(580, 40, window=mapa, anchor=W)

        status = Button(text="Status", font=self.fontPadrao, width=20, command=self.status)
        self.statusb = self.im.create_window(580, 70, window=status, anchor=W)

        x = {'PT': 'Salvar', 'EN': 'Save'}[self.idioma]
        save = Button(text=x, font=self.fontPadrao, width=20, command=self.save)
        self.saveb = self.im.create_window(580, 100, window=save, anchor=W)

        x = {'PT': 'Carregar', 'EN': 'Load'}[self.idioma]
        load = Button(text=x, font=self.fontPadrao, width=20, command=self.load)
        self.loadb = self.im.create_window(580, 130, window=load, anchor=W)

        x = {'PT': 'Opções', 'EN': 'Option'}[self.idioma]
        op = Button(text=x, font=self.fontPadrao, width=20, command=self.op)
        self.opb = self.im.create_window(580, 160, window=op, anchor=W)

        x = {'PT': 'Sair', 'EN': 'Exit'}[self.idioma]
        sair = Button(text=x, font=self.fontPadrao, width=20, command=self.fechar)
        self.sairb = self.im.create_window(580, 190, window=sair, anchor=W)

    def mapa(self):

        self.im.delete(self.mapab, self.statusb, self.saveb, self.loadb, self.opb, self.sairb)
        Mapa(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def status(self):

        self.im.delete(self.mapab, self.statusb, self.saveb, self.loadb, self.opb, self.sairb)
        Status(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def save(self):

        self.im.delete(self.mapab, self.statusb, self.saveb, self.loadb, self.opb, self.sairb)
        Save(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def load(self):
        
        self.im.delete(self.mapab, self.statusb, self.saveb, self.loadb, self.opb, self.sairb)
        Load(self.im, self.idioma, self.app, self.fontPadrao, self.p, False, False, self.mp)

    def op(self):

        self.im.delete(self.mapab, self.statusb, self.saveb, self.loadb, self.opb, self.sairb)
        OP(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def fechar(self):

        Exit(self.app)
