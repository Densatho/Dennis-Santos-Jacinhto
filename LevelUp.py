from tkinter import *
from FBase import *
from random import *
import Mapas


class LevelUp:

    def __init__(self, im, idioma, app, fontpadrao, p, mp, n, i):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp
        self.n = n
        self.i = i

        self.p[2][0] += 1
        self.p[2][1] += 20
        self.p[1].d += 3
        self.p[1].i += 3
        self.p[1].mm += 5
        self.p[1].m = self.p[1].mm
        self.p[1].vida_m += 5
        self.p[1].vida = self.p[1].vida_m
        self.p[1].t += 3
        self.p[1].r = self.p[1].r + 3
        self.p[1].s = self.p[1].s + 3
        self.p[3] = self.p[3] - self.p[4]
        self.p[4] = int(self.p[4] * 1.33)
        self.endb = 0
        self.info = 0
        self.botao()

    def botao(self):

        x = {'PT': 'VOCÊ SUBIU DE NÍVEL, PARABÊNS!', 'EN': 'LEVEL UP, CONGRATULATIONS!'}[self.idioma]
        self.info = self.im.create_text(570, 15, text=x, anchor=W, font=self.fontPadrao)

        x = {'PT': 'Continuar!', 'EN': 'Continue'}[self.idioma]
        end = Button(text=x, font=self.fontPadrao, width=20, command=self.end)
        self.endb = self.im.create_window(580, 40, window=end, anchor=W)

    def end(self):

        self.im.delete(self.info, self.endb)
        Mapas.Dungeons(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, self.n, self.i)
