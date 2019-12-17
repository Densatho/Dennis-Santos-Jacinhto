from tkinter import *
from FBase import *
from random import *
from LevelUp import *
import Fight
import Mapas
import Exit
import Menu


class Lutar:

    def __init__(self, im, idioma, app, fontpadrao, p, mp, n, i, teste, hih, m, dm):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp
        self.voltar = n
        self.i = i
        self.teste = teste
        self.hih = hih
        self.m = m
        self.dm = dm

        if self.p[1].s >= self.m.s:  # Velocidade
            txt = self.atkp()
            x = 595
            aux0 = True
        else:
            x = {'PT': 590, 'EN': 585}[self.idioma]
            txt = self.atkm()
            aux0 = False

        self.info = self.im.create_text(x, 15, text=txt, anchor=W, font=self.fontPadrao)

        if self.p[1].vida <= 0 or self.m.vida <= 0:
            x = {'PT': 'Continuar', 'EN': 'Continue'}[self.idioma]
            contb = Button(text=x, font=self.fontPadrao, width=20)
            if self.m.vida <= 0:
                contb["command"] = self.volta
            if self.p[1].vida <= 0:
                contb["command"] = self.fechar
            self.contB = self.im.create_window(580, 160, window=contb, anchor=W)

        else:
            if aux0:
                txt = self.atkm()
                x = {'PT': 590, 'EN': 585}[self.idioma]
            else:
                txt = self.atkp()
                x = 595

            self.label1 = self.im.create_text(x, 100, text=txt, anchor=W, font=self.fontPadrao)

            x = {'PT': 'Continuar', 'EN': 'Continue'}[self.idioma]
            contb = Button(text=x, font=self.fontPadrao, width=20)
            if self.p[1].vida <= 0 or self.m.vida <= 0:
                if self.m.vida <= 0:
                    contb["command"] = self.volta
                if self.p[1].vida <= 0:
                    contb["command"] = self.fechar
            else:
                contb["command"] = self.fight
            self.contB = self.im.create_window(580, 160, window=contb, anchor=W)

    def atkp(self):  # player
        
        aux_a = self.p[1].t-self.m.t
        if aux_a > 20:
            pc_a = (aux_a-20)*0.5
        elif aux_a < 0:
            pc_a = aux_a*2.0
        else:
            pc_a = 0
        r_a = 90+pc_a
        if r_a < 0:
            r_a = 0
        elif r_a > 95:
            r_a = 95
        r_a /= 100

        x = random()
        aux = dano(r_a, x, self.dm, self.m.r, self.p[1].d, self.hih)
        
        if aux > 0:
            self.m.vida -= aux
            x = {'PT': 'Você deu {} de dano', 'EN': 'You deal {} damage'}[self.idioma]
            return x.format(aux)
        else:
            y = {'PT': "Você errou o ataque", 'EN': 'You missed the attack'}[self.idioma]
            return y

    def atkm(self):
        
        aux_b = self.m.t-self.p[1].t
        if aux_b > 20:
            pc_b = (aux_b-20)*0.5
        elif aux_b < 0:
            pc_b = aux_b*2.0
        else:
            pc_b = 0
        r_b = 90+pc_b
        if r_b < 0:
            r_b = 0
        elif r_b > 95:
            r_b = 95
        r_b /= 100

        x = random()
        aux = dano(r_b, x, 0, self.p[1].r, self.m.d, False)  # monstro

        if aux > 0:
            self.p[1].vida -= aux
            x = {'PT': 'Você tomou {} de dano', 'EN': 'You take {} damage'}[self.idioma]
            return x.format(aux)
        else:
            y = {'PT': "Inimigo errou o ataque", 'EN': 'Enemy missed the attack'}[self.idioma]
            return y

    def volta(self):

        self.i += 1

        self.im.delete(self.info, self.contB)
        try:
            self.im.delete(self.label1)
        except AttributeError:
            pass

        self.p[3] += self.m.xp

        if self.p[3] >= self.p[4]:
            LevelUp(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, self.voltar, self.i)
        else:
            Mapas.Dungeons(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, self.voltar, self.i)

    def fechar(self):
        Exit.Exit(self.app)

    def fight(self):
        self.im.delete(self.info, self.contB)
        try:
            self.im.delete(self.label1)
        except AttributeError:
            pass
        Fight.Fight(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, self.voltar, self.i, 0, 0, True, self.m)
