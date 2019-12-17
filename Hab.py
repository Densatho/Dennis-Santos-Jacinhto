from tkinter import *
from FBase import *
import Menu
import Status


class Habilidades:

    def __init__(self, im, idioma, app, fontpadrao, p, teste, mp):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp
        self.teste = teste

        x = {'PT': 'HABILIDADES - Pontos de Habilidade disponiveis: {}', 'EN': 'SKILLS - Skill Points Available: {}'}

        self.info = self.im.create_text({'PT': 500, 'EN': 560}[self.idioma], 15,
                                        text=x[self.idioma].format(self.p[2][1]), anchor=W, font=self.fontPadrao)

        self.mV = ['F', 0]
        self.mA = ['F', 0]
        self.mVE = ['F', 0]
        self.mM = ['F', 0]
        self.mB = ['F', 0]
        self.mP = ['F', 0]

        for i in range(0, len(self.p[5])):
            if self.p[5][i].nome[0:-7] == 'Magia Vermelha':
                self.mV[0], self.mV[1] = letra(self.p[5][i].nome[-1]), i
            elif self.p[5][i].nome[0:-7] == 'Magia Azul':
                self.mA[0], self.mA[1] = letra(self.p[5][i].nome[-1]), i
            elif self.p[5][i].nome[0:-7] == 'Magia Verde':
                self.mVE[0], self.mVE[1] = letra(self.p[5][i].nome[-1]), i
            elif self.p[5][i].nome[0:-7] == 'Magia Marrom':
                self.mM[0], self.mM[1] = letra(self.p[5][i].nome[-1]), i
            elif self.p[5][i].nome[0:-7] == 'Magia Branca':
                self.mB[0], self.mB[1] = letra(self.p[5][i].nome[-1]), i
            elif self.p[5][i].nome[0:-7] == 'Magia Negra':
                self.mP[0], self.mA[1] = letra(self.p[5][i].nome[-1]), i

        if len(self.p[5]) == 0:
            self.mV[0] = 'F'
            self.mA[0] = 'F'
            self.mVE[0] = 'F'
            self.mM[0] = 'F'
            self.mB[0] = 'F'
            self.mP[0] = 'F'

        x = {'PT': 'Magia Vermelha Rank {}', 'EN': 'Red Magic Rank {}'}[self.idioma]
        h1 = Button(text=x.format(self.mV[0]),
                    font=self.fontPadrao, width=20)
        x = {'PT': 'Magia Azul Rank {}', 'EN': 'Blue Magic Rank {}'}[self.idioma]
        h2 = Button(text=x.format(self.mA[0]),
                    font=self.fontPadrao, width=20)
        x = {'PT': 'Magia Verde Rank {}', 'EN': 'Green Magic Rank {}'}[self.idioma]
        h3 = Button(text=x.format(self.mVE[0]),
                    font=self.fontPadrao, width=20)
        x = {'PT': 'Magia Marrom Rank {}', 'EN': 'Brown Magic Rank {}'}[self.idioma]
        h4 = Button(text=x.format(self.mM[0]),
                    font=self.fontPadrao, width=20)
        x = {'PT': 'Magia Branca Rank {}', 'EN': 'White Magic Rank {}'}[self.idioma]
        h5 = Button(text=x.format(self.mB[0]),
                    font=self.fontPadrao, width=20)
        x = {'PT': 'Magia Negra Rank {}', 'EN': 'Dark Magic Rank {}'}[self.idioma]
        h6 = Button(text=x.format(self.mP[0]),
                    font=self.fontPadrao, width=20)

        if self.mV[0] == 'S':
            h1['fg'] = 'white'
            h1['bg'] = 'gray'
            self.h1 = self.im.create_window(504, 40, window=h1, anchor=W)
        elif custo(self.mV[0]) <= self.p[2][1]:
            h1['command'] = self.hup1
            self.h1 = self.im.create_window(504, 40, window=h1, anchor=W)
        else:
            h1['fg'] = 'white'
            h1['bg'] = 'gray'
            self.h1 = self.im.create_window(504, 40, window=h1, anchor=W)

        if self.mA[0] == 'S':
            h2['fg'] = 'white'
            h2['bg'] = 'gray'
            self.h2 = self.im.create_window(676, 40, window=h2, anchor=W)
        elif custo(self.mA[0]) <= self.p[2][1]:
            h2['command'] = self.hup2
            self.h2 = self.im.create_window(676, 40, window=h2, anchor=W)
        else:
            h2['fg'] = 'white'
            h2['bg'] = 'gray'
            self.h2 = self.im.create_window(676, 40, window=h2, anchor=W)

        if True:   # self.mVE[0] == 'S'
            h3['fg'] = 'white'
            h3['bg'] = 'gray'
            self.h3 = self.im.create_window(504, 70, window=h3, anchor=W)
        """ elif custo(self.mVE[0]) <= self.p[2][1]:
            h3['command'] = self.hup3
            self.h3 = self.im.create_window(504, 70, window=h3, anchor=W)         
        else:
            h3['fg'] = 'white'
            h3['bg'] = 'gray'
            self.h3 = self.im.create_window(504, 70, window=h3, anchor=W)"""

        if True:   # self.mM[0] == 'S'
            h4['fg'] = 'white'
            h4['bg'] = 'gray'
            self.h4 = self.im.create_window(676, 70, window=h4, anchor=W)
        """elif custo(self.mM[0]) <= self.p[2][1]:
            h4['command'] = self.hup4
            self.h4 = self.im.create_window(676, 70, window=h4, anchor=W)            
        else:
            h4['fg'] = 'white'
            h4['bg'] = 'gray'
            self.h4 = self.im.create_window(676, 70, window=h4, anchor=W)"""

        if True:   # self.mB[0] == 'S'
            h5['fg'] = 'white'
            h5['bg'] = 'gray'
            self.h5 = self.im.create_window(504, 100, window=h5, anchor=W)
        """elif custo(self.mB[0]) <= self.p[2][1]:
            h5['command'] = self.hup5
            self.h5 = self.im.create_window(504, 100, window=h5, anchor=W) 
        else:
            h5['fg'] = 'white'
            h5['bg'] = 'gray'
            self.h5 = self.im.create_window(504, 100, window=h5, anchor=W) """

        if True:   # self.mP[0] == 'S'
            h6['fg'] = 'white'
            h6['bg'] = 'gray'
            self.h6 = self.im.create_window(676, 100, window=h6, anchor=W)
        """elif custo(self.mP[0]) <= self.p[2][1]:
            h6['command'] = self.hup6
            self.h6 = self.im.create_window(676, 100, window=h6, anchor=W)
        else:
            h6['fg'] = 'white'
            h6['bg'] = 'gray'
            self.h6 = self.im.create_window(676, 100, window=h6, anchor=W)"""

        if not self.teste:
            x = {'PT': 'Fechar Habilidades', 'EN': 'Close Skills'}
            sair = Button(text=x[self.idioma], font=self.fontPadrao, width=20, command=self.fhab)
            self.sair = self.im.create_window(590, 130, window=sair, anchor=W)

        self.x = 0

    def hup1(self):
        if self.mV[0] == 'F':
            self.p[5].append(Fogo(self.mV[0]))
        else:
            self.p[5][self.mV[1]] = (Fogo(self.mV[0]))
        self.p[2][1] -= custo(self.mV[0])
        self.im.delete(self.info, self.h1, self.h2, self.h3, self.h4, self.h5, self.h6)

        if not self.teste:
            self.im.delete(self.sair)

        if not self.teste:
            Habilidades(self.im, self.idioma, self.app, self.fontPadrao, self.p, False, self.mp)
        else:
            Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def hup2(self):
        if self.mA[0] == 'F':
            self.p[5].append(Agua(self.mA[0]))
        else:
            self.p[5][self.mA[1]] = (Agua(self.mA[0]))
        self.p[2][1] -= custo(self.mA[0])
        self.im.delete(self.info, self.h1, self.h2, self.h3, self.h4, self.h5, self.h6)

        if not self.teste:
            self.im.delete(self.sair)

        if not self.teste:
            Habilidades(self.im, self.idioma, self.app, self.fontPadrao, self.p, False, self.mp)
        else:
            Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def hup3(self):
        self.x = 1
        self.x += 2
        print(self.x)

    def hup4(self):
        self.x = 1
        self.x += 2
        print(self.x)

    def hup5(self):
        self.x = 1
        self.x += 2
        print(self.x)
        
    def hup6(self):
        self.x = 1
        self.x += 2
        print(self.x)
            
    def fhab(self):

        self.im.delete(self.info, self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.sair)
        Status.Status(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)
