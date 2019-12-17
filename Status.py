from tkinter import *
from FBase import *
import Hab
import Menu


class Status:

    def __init__(self, im, idioma, app, fontpadrao, p, mp):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp

        aux = (self.p[3] / self.p[4])
        aux = int(10*aux)
        xp = '|'
        for i in range(0, aux):
            xp += '='
        for i in range(0, 10-aux):
            xp += '-'
        xp += '|'

        txt1 = ''
        posicao = 0
        for i in range(0, len(self.p[5])):
            if self.p[5][i].nome[0:-7] == 'Magia Vermelha':
                x = {'PT': 'Magia Vermelha Rank', 'EN': '   Red Magic Rank'}[self.idioma]
                xn = {'PT': '\n', 'EN': '  \n'}[self.idioma]
                txt1 += x + p[5][i].nome[-2:] + xn
                posicao += 1
            elif self.p[5][i].nome[0:-7] == 'Magia Azul':
                x = {'PT': '  Magia Azul Rank', 'EN': '  Blue Magic Rank'}[self.idioma]
                txt1 += x + p[5][i].nome[-2:] + '  \n'
                posicao += 1
            elif self.p[5][i].nome[0:-7] == 'Magia Verde':
                x = {'PT': '  Magia Verde Rank', 'EN': '  Green Magic Rank'}[self.idioma]
                txt1 += x + p[5][i].nome[-2:] + ' \n'
                posicao += 1
            elif self.p[5][i].nome[0:-7] == 'Magia Marrom':
                x = {'PT': ' Magia Marrom Rank', 'EN': '  Brown Magic Rank'}[self.idioma]
                txt1 += x + p[5][i].nome[-2:] + ' \n'
                posicao += 1
            elif self.p[5][i].nome[0:-7] == 'Magia Branca':
                x = {'PT': ' Magia Branca Rank', 'EN': '  White Magic Rank'}[self.idioma]
                txt1 += x + p[5][i].nome[-2:] + ' \n'
                posicao += 1
            elif self.p[5][i].nome[0:-7] == 'Magia Negra':
                x = {'PT': '  Magia Negra Rank', 'EN': '  Dark Magic Rank'}[self.idioma]
                xn = {'PT': ' \n', 'EN': '  \n'}[self.idioma]
                txt1 += x + p[5][i].nome[-2:] + xn
                posicao += 1

        x1 = '''Nickname: {}\n\nSkill Points: {}\n\n Life: {}/{}   ||  Mana:     {}/{}\n
        Strength: {}   ||  Intelligence:     {} \n\n Resist:      {} || Speed:      {}      \n
        Technique: {}    ||  Level:          {}    \n
        Exp: {} {}/{}      \n\n      Skills:      \n{}'''

        x2 = '''Apelido: {}\n\nPontos de Habilidade disponiveis: {}\n\n Vida: {}/{}   ||  Mana:     {}/{}\n
        Força:    {}   ||  Inteligencia: {} \n\n Resistencia: {} || Velocidade: {}      \n
        Tecnica:   {}    ||  Nivel:          {}    \n
        Exp: {} {}/{}      \n
        Habilidades:        \n{}'''

        txt = {'PT': x2, 'EN': x1}[self.idioma]

        txt = txt.format(self.p[0], self.p[2][1], self.p[1].vida, self.p[1].vida_m, self.p[1].m, self.p[1].mm,
                         self.p[1].d, self.p[1].i, self.p[1].r, self.p[1].s, self.p[1].t, self.p[2][0], xp, self.p[3],
                         self.p[4], txt1)

        posicao *= 10

        info = Label(text=txt, font=self.fontPadrao, fg='white', bg='black')
        self.info = self.im.create_window({'PT': 540, 'EN': 535}[self.idioma], 140 + posicao, anchor=W, window=info)

        x = {'PT': "Abrir Arvore de\nHabilidades", 'EN': 'Open Skills\nTree'}[self.idioma]
        hab = Button(text=x, font=self.fontPadrao, width=20, command=self.hab,
                     fg='white', bg='black')
        self.habb = self.im.create_window(580, 305 + (posicao * 1.5), window=hab, anchor=W)

        x = {'PT': "Voltar", 'EN': 'Back'}[self.idioma]
        end = Button(text=x, font=self.fontPadrao, width=20, command=self.endstatus, fg='white', bg='black')
        self.endstatusB = self.im.create_window(580, 345 + (posicao * 1.5), window=end, anchor=W)

    def endstatus(self):

        self.im.delete(self.info, self.habb, self.endstatusB)
        Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def hab(self):

        self.im.delete(self.info, self.habb, self.endstatusB)
        Hab.Habilidades(self.im, self.idioma, self.app, self.fontPadrao, self.p, False, self.mp)
