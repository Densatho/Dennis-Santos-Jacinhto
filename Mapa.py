from tkinter import *
from FBase import *
from Mapas import *
import Menu


class Mapa:

    def __init__(self, im, idioma, app, fontpadrao, p, mp):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp
        mpa = [{'PT': 'Planície', 'EN': 'Plain'},
               {'PT': 'Pântano\n(Nv5 recomendado)', 'EN': 'Swamp\n(Lv5 recommended)'},
               {'PT': 'Caverna\n(Nv10 recomendado)', 'EN': 'Cave\n(Lv10 recommended)'},
               {'PT': 'Savana\n(Nv20 recomendado)', 'EN': 'Savanna\n(Lv20 recommended)'},
               {'PT': 'Profundesas da caverna\n(Nv30 recomendado)', 'EN': 'Cave Depth\nLv30 recommended)'}]

        x = {'PT': "Selecione a dungeon que deseja entrar:", 'EN': 'Select a dungeon to go:'}[self.idioma]
        self.info = self.im.create_text({'PT': 540, 'EN': 590}[self.idioma], 15, text=x, anchor=W, font=self.fontPadrao)

        op1 = Button(text=mpa[0][self.idioma], font=self.fontPadrao, width=20, bg='white', fg='black', command=self.p1)
        self.op1b = self.im.create_window(580, 40, window=op1, anchor=W)

        op2 = Button(text=mpa[1][self.idioma], font=self.fontPadrao, width=20, bg='gray', fg='white')
        if self.mp > 1:
            op2['bg'] = 'white'
            op2['fg'] = 'black'
            op2['command'] = self.p2
        self.op2b = self.im.create_window(580, 78, window=op2, anchor=W)

        op3 = Button(text=mpa[2][self.idioma], font=self.fontPadrao, width=20, bg='gray', fg='white')
        if self.mp > 2:
            op3['bg'] = 'white'
            op3['fg'] = 'black'
            op3['command'] = self.p3
        self.op3b = self.im.create_window(580, 124, window=op3, anchor=W)

        op4 = Button(text=mpa[3][self.idioma], font=self.fontPadrao, width=20, bg='gray', fg='white')
        if self.mp > 3:
            op4['bg'] = 'white'
            op4['fg'] = 'black'
            op4['command'] = self.p4
        self.op4b = self.im.create_window(580, 170, window=op4, anchor=W)

        op5 = Button(text=mpa[4][self.idioma], font=self.fontPadrao, width=20, bg='gray', fg='white')
        if self.mp > 4:
            op5['bg'] = 'white'
            op5['fg'] = 'black'
            op5['command'] = self.p5
        self.op5b = self.im.create_window(580, 216, window=op5, anchor=W)

        x = {'PT': "Voltar", 'EN': 'Back'}[self.idioma]
        exitb = Button(text=x, font=self.fontPadrao, width=20, command=self.menu)
        self.exit = self.im.create_window(580, 254, window=exitb, anchor=W)

    def p1(self):

        self.im.delete(self.info, self.op1b, self.op2b, self.op3b, self.op4b, self.op5b, self.exit)
        Dungeons(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, 1, 0)

    def p2(self):

        self.im.delete(self.info, self.op1b, self.op2b, self.op3b, self.op4b, self.op5b, self.exit)
        Dungeons(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, 2, 0)

    def p3(self):

        self.im.delete(self.info, self.op1b, self.op2b, self.op3b, self.op4b, self.op5b, self.exit)
        Dungeons(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, 3, 0)

    def p4(self):

        self.im.delete(self.info, self.op1b, self.op2b, self.op3b, self.op4b, self.op5b, self.exit)
        Dungeons(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, 4, 0)

    def p5(self):

        self.im.delete(self.info, self.op1b, self.op2b, self.op3b, self.op4b, self.op5b, self.exit)
        Dungeons(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, 5, 0)

    def menu(self):

        self.im.delete(self.info, self.op1b, self.op2b, self.op3b, self.op4b, self.op5b, self.exit)
        Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)
