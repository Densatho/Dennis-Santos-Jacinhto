from tkinter import *
from FBase import *
from random import *
from Luta import *


class Fight:

    def __init__(self, im, idioma, app, fontpadrao, p, mp, n, i, nvm, rad, teste, m):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp
        self.n = n
        self.i = i
        self.nvm = nvm
        self.rad = rad
        self.teste = teste

        if not self.teste:
            self.m = Monster(self.nvm, self.rad)
            self.teste = False
        else:
            self.m = m

        x = {'PT': 'nv', 'EN': 'lv'}[self.idioma]
        x = "{} {}{} - HP: {}/{}".format(self.m.nome, x, self.m.nv, self.m.vida, self.m.vida_m)
        self.info = self.im.create_text(600, 15, text=x, anchor=W, font=self.fontPadrao)

        x = {'PT': 'nv', 'EN': 'lv'}[self.idioma]
        x = '{} {}{} - HP: {}/{} | MP: {}/{}'.format(self.p[0], x, self.p[2][0], self.p[1].vida, self.p[1].vida_m,
                                                     self.p[1].m, self.p[1].mm)
        self.playerL = self.im.create_text(560, 100, text=x, anchor=W, font=self.fontPadrao)

        x = {'PT': 'Ataque', 'EN': 'Attack'}[self.idioma]
        atkb = Button(text=x, font=self.fontPadrao, width=10, command=self.atk)
        self.atkb = self.im.create_window(580, 130, window=atkb, anchor=W)

        x = {'PT': 'Habilidades', 'EN': 'Skills'}[self.idioma]
        apb = Button(text=x, font=self.fontPadrao, width=10, command=self.ap)
        self.apb = self.im.create_window(680, 130, window=apb, anchor=W)

        self.hih = False
        self.AZUt = False
        self.VERt = False
        self.men = False

        self.VE = [0, 0]
        self.AZ = [0, 0]
        self.VD = [0, 0]
        self.MA = [0, 0]
        self.BR = [0, 0]
        self.NE = [0, 0]
        self.veb = 0
        self.azb = 0
        self.vdb = 0
        self.mab = 0
        self.brb = 0
        self.neb = 0
        self.VER = 0
        self.AZU = 0
        self.ef = 0
        self.dm = 0
        self.x = 0
        self.y = 0
        self.contv = 0
        self.contaz = 0

    def ap(self):

        self.im.delete(self.apb)

        if not self.men:

            self.men = True
            x = {'PT': 'Habilidades', 'EN': 'Skills'}[self.idioma]
            apb = Button(text=x, font=self.fontPadrao, width=10, fg='white', bg='gray', command=self.ap)
            self.apb = self.im.create_window(680, 130, window=apb, anchor=W)

            aux = len(self.p[5])
            for i in range(0, aux):
                if self.p[5][i].nome[0:-7] == 'Magia Vermelha':
                    self.VE[0], self.VE[1] = i, True
                elif self.p[5][i].nome[0:-7] == 'Magia Azul':
                    self.AZ[0], self.AZ[1] = i, True
                elif self.p[5][i].nome[0:-7] == 'Magia Verde':
                    self.VD[0], self.VD[1] = i, True
                elif self.p[5][i].nome[0:-7] == 'Magia Marrom':
                    self.MA[0], self.MA[1] = i, True
                elif self.p[5][i].nome[0:-7] == 'Magia Branca':
                    self.BR[0], self.BR[1] = i, True
                elif self.p[5][i].nome[0:-7] == 'Magia Negra':
                    self.PR[0], self.PR[1] = i, True

            self.x, self.y = [580, 680, 580, 680, 580, 680], [170, 170, 210, 210, 240, 240]
            cont = 0

            if self.VE[1]:
                x = {'PT': 'Magia\nVermelha', 'EN': 'Red\nMagic'}[self.idioma]
                veb = Button(text=x, font=self.fontPadrao, width=10, command=self.vermelho)
                self.veb = self.im.create_window(self.x[cont], self.y[cont], window=veb, anchor=W)
                self.contv = cont
                cont += 1

            if self.AZ[1]:
                x = {'PT': 'Magia\nAzul', 'EN': 'Blue\nMagic'}[self.idioma]
                azb = Button(text=x, font=self.fontPadrao, width=10, command=self.azul)
                self.azb = self.im.create_window(self.x[cont], self.y[cont], window=azb, anchor=W)
                self.contaz = cont
                cont += 1

            if self.VD[1]:
                x = {'PT': 'Magia\nVerde', 'EN': 'Green\nMagic'}[self.idioma]
                vdb = Button(text=x, font=self.fontPadrao, width=10, command=self.verde)
                self.vdb = self.im.create_window(self.x[cont], self.y[cont], window=vdb, anchor=W)
                cont += 1

            if self.MA[1]:
                x = {'PT': 'Magia\nMarrom', 'EN': 'Brown\nMagic'}[self.idioma]
                mab = Button(text=x, font=self.fontPadrao, width=10, command=self.marrom)
                self.mab = self.im.create_window(self.x[cont], self.y[cont], window=mab, anchor=W)
                cont += 1

            if self.BR[1]:
                x = {'PT': 'Magia\nBranca', 'EN': 'White\nMagic'}[self.idioma]
                brb = Button(text="Magia\nBranca", font=self.fontPadrao, width=10, command=self.branca)
                self.brb = self.im.create_window(self.x[cont], self.y[cont], window=brb, anchor=W)
                cont += 1

            if self.NE[1]:
                x = {'PT': 'Magia\nNegra', 'EN': 'Dark\nMagic'}[self.idioma]
                neb = Button(text="Magia\nNegra", font=self.fontPadrao, width=10, command=self.negra)
                self.neb = self.im.create_window(self.x[cont], self.y[cont], window=neb, anchor=W)

        else:

            self.men = False
            self.im.delete(self.veb, self.azb)

            x = {'PT': 'Habilidades', 'EN': 'Skills'}[self.idioma]
            apb = Button(text=x, font=self.fontPadrao, width=10, command=self.ap)
            self.apb = self.im.create_window(680, 130, window=apb, anchor=W)

    def vermelho(self):

        self.VERt = True
        self.VER = Tk()
        self.VER.title(self.p[5][self.VE[0]].nome)
        self.VER.configure(background='dark red')

        self.im.delete(self.veb)
        x = {'PT': 'Magia\nVermelha', 'EN': 'Red\nMagic'}[self.idioma]
        veb = Button(text=x, font=self.fontPadrao, width=10, bg='gray', fg='white')
        self.veb = self.im.create_window(self.x[self.contv], self.y[self.contv], window=veb, anchor=W)
        
        ve1 = Frame(self.VER)
        ve1["pady"] = 20
        ve1["bg"] = 'dark red'
        ve1.pack()

        ve2 = Frame(self.VER)
        ve2["padx"] = 20
        ve2["bg"] = 'dark red'
        ve2.pack()

        ve3 = Frame(self.VER)
        ve3["bg"] = 'dark red'
        ve3["padx"] = 20
        ve3.pack()

        info = Label(ve1, text=self.p[5][self.VE[0]].nome, font=self.fontPadrao, bg='dark red')
        info.pack()

        aux = len(self.p[5][self.VE[0]].a)
        
        if self.p[1].m >= self.p[5][self.VE[0]].a[0].mc:
            b1 = Button(ve2)
            b1["bg"] = 'red'
            b1["text"] = self.p[5][self.VE[0]].a[0].nome
            b1["font"] = self.fontPadrao
            b1["width"] = 10
            b1["command"] = self.fogo1
            b1.pack(side=LEFT)
        if aux > 1:
            if aux >= 2 and self.p[1].m >= self.p[5][self.VE[0]].a[1].mc:
                b2 = Button(ve2)
                b2["text"] = self.p[5][self.VE[0]].a[1].nome
                b2["bg"] = 'red'
                b2["font"] = self.fontPadrao
                b2["width"] = 10
                b2["command"] = self.fogo2
                b2.pack(side=LEFT)
            if aux >= 3 and self.p[1].m >= self.p[5][self.VE[0]].a[2].mc:
                b3 = Button(ve3)
                b3["text"] = self.p[5][self.VE[0]].a[2].nome
                b3["bg"] = 'red'
                b3["font"] = self.fontPadrao
                b3["width"] = 10
                b3["command"] = self.fogo3
                b3.pack(side=LEFT)

    def fogo1(self):

        self.ef = verific(self.p[5][self.VE[0]].a[0].effect)
        self.dm, self.p[1].m = atkb(0, self.VE[0], self.p[1].m, self.p)
        self.hih = True
        self.atk()

    def fogo2(self):

        self.ef = verific(self.p[5][self.VE[0]].a[0].effect)
        self.dm, self.p[1].m = atkb(1, self.VE[0], self.p[1].m, self.p)
        self.hih = True
        self.atk()

    def fogo3(self):

        self.ef = verific(self.p[5][self.VE[0]].a[0].effect)
        self.dm, self.p[1].m = atkb(2, self.VE[0], self.p[1].m, self.p)
        self.hih = True
        self.atk()

    def azul(self):

        self.AZUt = True
        self.AZU = Tk()
        self.AZU.title(self.p[5][self.AZ[0]].nome)
        self.AZU.configure(background='dark blue')

        self.im.delete(self.azb)
        x = {'PT': 'Magia\nAzul', 'EN': 'Blue\nMagic'}[self.idioma]
        azb = Button(text=x, font=self.fontPadrao, width=10, bg='gray', fg='white')
        self.azb = self.im.create_window(self.x[self.contaz], self.y[self.contaz], window=azb, anchor=W)

        az1 = Frame(self.AZU)
        az1["pady"] = 20
        az1["bg"] = 'dark blue'
        az1.pack()

        az2 = Frame(self.AZU)
        az2["padx"] = 20
        az2["bg"] = 'dark blue'
        az2.pack()

        az3 = Frame(self.AZU)
        az3["padx"] = 20
        az3["bg"] = 'dark blue'
        az3.pack()

        az4 = Frame(self.AZU)
        az4["padx"] = 20
        az4["bg"] = 'dark blue'
        az4.pack()

        az5 = Frame(self.AZU)
        az5["padx"] = 20
        az5["bg"] = 'dark blue'
        az5.pack()

        az6 = Frame(self.AZU)
        az6["padx"] = 20
        az6["bg"] = 'dark blue'
        az6.pack()

        info = Label(az1, text=self.p[5][self.AZ[0]].nome, font=self.fontPadrao, bg='dark blue')
        info.pack()

        aux = len(self.p[5][self.AZ[0]].a)
        
        if self.p[1].m >= self.p[5][self.AZ[0]].a[0].mc:
            b1 = Button(az2)
            b1["bg"] = 'blue'
            b1["text"] = self.p[5][self.AZ[0]].a[0].nome
            b1["font"] = self.fontPadrao
            b1["width"] = 10
            b1["command"] = self.azul1
            b1.pack(side=LEFT)
        if aux > 1:
            if aux >= 2 and self.p[1].m >= self.p[5][self.AZ[0]].a[1].mc:
                b2 = Button(az2)
                b2["bg"] = 'blue'
                b2["text"] = self.p[5][self.AZ[0]].a[1].nome
                b2["font"] = self.fontPadrao
                b2["width"] = 10
                b2["command"] = self.azul2
                b2.pack(side=LEFT)
            if aux >= 3 and self.p[1].m >= self.p[5][self.AZ[0]].a[2].mc:
                b3 = Button(az3)
                b3["bg"] = 'blue'
                b3["text"] = self.p[5][self.AZ[0]].a[2].nome
                b3["font"] = self.fontPadrao
                b3["width"] = 10
                b3["command"] = self.azul3
                b3.pack(side=LEFT)

    def azul1(self):

        self.ef = verific(self.p[5][self.VE[0]].a[0].effect)
        self.dm, self.p[1].m = atkb(0, self.AZ[0], self.p[1].m, self.p)
        self.hih = True
        self.atk()

    def azul2(self):

        self.ef = verific(self.p[5][self.VE[0]].a[0].effect)
        self.dm, self.p[1].m = atkb(1, self.AZ[0], self.p[1].m, self.p)
        self.hih = True
        self.atk()

    def azul3(self):

        self.ef = verific(self.p[5][self.VE[0]].a[0].effect)
        self.dm, self.p[1].m = atkb(2, self.AZ[0], self.p[1].m, self.p)
        self.hih = True
        self.atk()

    def atk(self):

        if self.VERt:
            try:
                self.VER.destroy()
            except TclError:
                pass

        if self.AZUt:
            try:
                self.AZU.destroy()
            except TclError:
                pass

        self.im.delete(self.info, self.playerL, self.atkb, self.apb)
        self.im.delete(self.veb, self.azb)
        
        Lutar(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp, self.n, self.i, self.teste, self.hih,
              self.m, self.dm)
