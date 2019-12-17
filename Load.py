from tkinter import *
from FBase import *
import Menu
import Menu_Inicial


class Load:

    def __init__(self, im, idioma, app, fontpadrao, p, teste1, teste2, mp):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp
        self.teste = teste1

        if not teste2:
            txt = {'PT': "Selecione o Slot que deseja carregar:", 'EN': 'Select a slot to loading:'}[self.idioma]
            x = {'PT': 550, 'EN': 590}[self.idioma]
        else:
            txt = {'PT': "Slot Invalido, escolha outro:", 'EN': 'Invalid Slot, Choose Another:'}[self.idioma]
            x = {'PT': 575, 'EN': 570}[self.idioma]

        self.info = self.im.create_text(x, 15, text=txt, anchor=W, font=self.fontPadrao)

        arq = open('saves\\Slot 1.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot1 = Button(text='Slot 1 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot1l)
        self.slot1 = self.im.create_window(580, 40, window=slot1, anchor=W)

        arq = open('saves\\Slot 2.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot2 = Button(text='Slot 2 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot2l)
        self.slot2 = self.im.create_window(580, 70, window=slot2, anchor=W)

        arq = open('saves\\Slot 3.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot3 = Button(text='Slot 3 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot3l)
        self.slot3 = self.im.create_window(580, 100, window=slot3, anchor=W)

        arq = open('saves\\Slot 4.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot4 = Button(text='Slot 4 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot4l)
        self.slot4 = self.im.create_window(580, 130, window=slot4, anchor=W)

        arq = open('saves\\Slot 5.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot5 = Button(text='Slot 5 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot5l)
        self.slot5 = self.im.create_window(580, 160, window=slot5, anchor=W)
        arq.close()

        x = {'PT': "Voltar", 'EN': 'Back'}[self.idioma]
        sair = Button(text=x, font=self.fontPadrao, width=20)
        if not self.teste:
            sair["command"] = self.menu
        else:
            sair["command"] = self.inicio
        self.sair = self.im.create_window(580, 190, window=sair, anchor=W)

        self.aux = 0

    def inicio(self):

        self.im.delete(self.info, self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.sair)
        Menu_Inicial.Inicio(self.im, self.idioma, self.app, self.fontPadrao)

    def menu(self):

        self.im.delete(self.info, self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.sair)
        Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def slot1l(self):
        self.aux = 'saves\\Slot 1.svt'
        self.carregar()

    def slot2l(self):
        self.aux = 'saves\\Slot 2.svt'
        self.carregar()

    def slot3l(self):
        self.aux = 'saves\\Slot 3.svt'
        self.carregar()

    def slot4l(self):
        self.aux = 'saves\\Slot 4.svt'
        self.carregar()

    def slot5l(self):
        self.aux = 'saves\\Slot 5.svt'
        self.carregar()

    def carregar(self):
        arq = open(self.aux, 'r')
        del self.aux
        arql = arq.readlines()

        if len(arql) < 2:
            self.im.delete(self.info, self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.sair)
            Load(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.teste, True, self.mp)

        else:
            if len(self.p) > 2:
                del self.p
            
            self.p = ['---']
            self.p.append(Player())
            self.p.append([1, 0])
            self.p.append(0)
            self.p.append(25)
            self.p.append([])
            self.mp = 1

            self.p[0] = arql[0][0:-1]
            self.p[1].vida = int(arql[1][0:-1])
            self.p[1].vida_m = int(arql[2][0:-1])
            self.p[1].m = int(arql[3][0:-1])
            self.p[1].mm = int(arql[4][0:-1])
            self.p[1].d = int(arql[5][0:-1])
            self.p[1].i = int(arql[6][0:-1])
            self.p[1].t = int(arql[7][0:-1])
            self.p[1].s = int(arql[8][0:-1])
            self.p[1].r = int(arql[9][0:-1])
            aux, aux1 = (arql[10][0:-1]).split('-')
            self.p[2][0], self.p[2][1] = int(aux), int(aux1)
            self.p[3] = int(arql[11][0:-1])
            self.p[4] = int(arql[12][0:-1])
            self.mp = int(arql[13][0:-1])

            m_v = [False, 0, 0]
            m_a = [False, 0, 0]
            m_ve = [False, 0, 0]
            m_m = [False, 0, 0]
            m_b = [False, 0, 0]
            m_n = [False, 0, 0]

            for i in range(0, len(arql)-14):
                if arql[14+i][0:-8] == 'Magia Vermelha':
                    m_v = [True, arql[14+i][-2], i]
                elif arql[14+i][0:-8] == 'Magia Azul':
                    m_a = [True, arql[14+i][-2], i]
                elif arql[14+i][0:-8] == 'Magia Verde':
                    m_ve = [True, arql[14+i][-2], i]
                elif arql[14+i][0:-8] == 'Magia Marrom':
                    m_m = [True, arql[14+i][-2], i]
                elif arql[14+i][0:-8] == 'Magia Branca':
                    m_b = [True, arql[14+i][-2], i]
                elif arql[14+i][0:-8] == 'Magia Negra':
                    m_n = [True, arql[14+i][-2], i]
                
            for i in range(0, 6):
                if m_v[0] and m_v[2] == i:
                    self.p[5].append(Fogo(m_v[1]))
                elif m_a[0] and m_a[2] == i:
                    self.p[5].append(Agua(m_a[1]))
                elif m_ve[0] and m_ve[2] == i:
                    self.p[5].append(Fogo(m_ve[1]))
                elif m_m[0] and m_m[2] == i:
                    self.p[5].append(Fogo(m_m[1]))
                elif m_b[0] and m_b[2] == i:
                    self.p[5].append(Fogo(m_b[1]))
                elif m_n[0] and m_n[2] == i:
                    self.p[5].append(Fogo(m_n[1]))

            self.menu()
