from tkinter import *
from FBase import *
from Fight import *
from random import *
import Mapa
import Menu


class Dungeons:

    def __init__(self, im, idioma, app, fontpadrao, p, mp, n, i):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp
        self.n = n
        self.i = i

        self.simt = {'PT': 'Sim', 'EN': 'Yes'}[self.idioma]
        self.naot = {'PT': 'Não', 'EN': 'No'}[self.idioma]

        if self.i < 5:

            self.y = {'1': 'st', '2': 'nd', '3': 'rd', '4': 'th', '5': 'th'}[str(self.i + 1)]
            self.x1 = {'PT': "Deseja entrar na {}º batalha?",
                       'EN': "Do you want to enter the {}{} battle?"}[self.idioma]
            if self.idioma == 'EN':
                self.x1 = self.x1.format(self.i + 1, self.y)
            else:
                self.x1 = self.x1.format(self.i + 1)

            if self.n == 1:
                self.n1()
            elif self.n == 2:
                self.n2()
            elif self.n == 3:
                self.n3()
            elif self.n == 4:
                self.n4()
            elif self.n == 5:
                self.n5()
        else:

            if self.n == 1 and self.mp == 1:
                self.mp = 2
            elif self.n == 2 and self.mp == 2:
                self.mp = 3
            elif self.n == 3 and self.mp == 3:
                self.mp = 4
            elif self.n == 4 and self.mp == 4:
                self.mp = 5

            x = {'PT': "Dungeon Finalizada", 'EN': "Dungeon Completed"}[self.idioma]
            self.info = self.im.create_text(600, 15, text=x, anchor=W, font=self.fontPadrao)

            x = {'PT': "Continuar", 'EN': "Next"}[self.idioma]
            cont = Button(text=x, font=self.fontPadrao, width=20, command=self.menu)
            self.contb = self.im.create_window(580, 40, window=cont, anchor=W)
            self.x = False
            self.sim = 0
            self.nao = 0
            self.nvm = 0
            self.rad = 0
    
    def menu(self):

        self.im.delete(self.info)

        if self.x:
            self.im.delete(self.sim, self.nao)
        else:
            self.im.delete(self.contb)
        Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)
        
    def n1(self):

        self.x = True
        self.nvm = randrange(1+self.i, 3+self.i)
        self.rad = 0

        self.info = self.im.create_text({'PT': 585, 'EN': 565}[self.idioma], 15, text=self.x1, anchor=W,
                                        font=self.fontPadrao)

        simb = Button(text=self.simt, font=self.fontPadrao, width=10, command=self.fight)
        self.sim = self.im.create_window(580, 40, window=simb, anchor=W)

        naob = Button(text=self.naot, font=self.fontPadrao, width=10, command=self.menu)
        self.nao = self.im.create_window(680, 40, window=naob, anchor=W)

    def n2(self):

        self.x = True
        self.nvm = randrange(6+self.i, 8+self.i)
        self.rad = randrange(0, 10)
        
        self.info = self.im.create_text({'PT': 585, 'EN': 565}[self.idioma], 15, text=self.x1, anchor=W,
                                        font=self.fontPadrao)

        simb = Button(text=self.simt, font=self.fontPadrao, width=10, command=self.fight)
        self.sim = self.im.create_window(580, 40, window=simb, anchor=W)

        naob = Button(text=self.naot, font=self.fontPadrao, width=10, command=self.menu)
        self.nao = self.im.create_window(680, 40, window=naob, anchor=W)

    def n3(self):

        self.x = True
        self.nvm = randrange(11+self.i, 14+self.i)
        self.rad = randrange(6, 10)
        
        self.info = self.im.create_text({'PT': 585, 'EN': 565}[self.idioma], 15, text=self.x1, anchor=W,
                                        font=self.fontPadrao)

        simb = Button(text=self.simt, font=self.fontPadrao, width=10, command=self.fight)
        self.sim = self.im.create_window(580, 40, window=simb, anchor=W)

        naob = Button(text=self.naot, font=self.fontPadrao, width=10, command=self.menu)
        self.nao = self.im.create_window(680, 40, window=naob, anchor=W)

    def n4(self):

        self.x = True
        self.nvm = randrange(20+self.i, 25+self.i)
        self.rad = randrange(6, 15)
        
        self.info = self.im.create_text({'PT': 585, 'EN': 565}[self.idioma], 15, text=self.x1, anchor=W,
                                        font=self.fontPadrao)

        simb = Button(text=self.simt, font=self.fontPadrao, width=10, command=self.fight)
        self.sim = self.im.create_window(580, 40, window=simb, anchor=W)

        naob = Button(text=self.naot, font=self.fontPadrao, width=10, command=self.menu)
        self.nao = self.im.create_window(680, 40, window=naob, anchor=W)

    def n5(self):

        self.x = True
        self.nvm = randrange(30+self.i, 36+self.i)
        self.rad = randrange(9, 17)
        
        self.info = self.im.create_text({'PT': 585, 'EN': 565}[self.idioma], 15, text=self.x1, anchor=W,
                                        font=self.fontPadrao)

        simb = Button(text=self.simt, font=self.fontPadrao, width=10, command=self.fight)
        self.sim = self.im.create_window(580, 40, window=simb, anchor=W)

        naob = Button(text=self.naot, font=self.fontPadrao, width=10, command=self.menu)
        self.nao = self.im.create_window(680, 40, window=naob, anchor=W)

    def fight(self):
        
        self.im.delete(self.info, self.sim, self.nao)
        Fight(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, self.n, self.i, self.nvm,
              self.rad, False, 0)
