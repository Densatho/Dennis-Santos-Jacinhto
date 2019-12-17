from tkinter import *
import Menu


class OP:

    def __init__(self, im, idioma, app, fontpadrao, p, mp):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp

        arq = open('config.svtg', 'r')
        config = arq.readlines()
        arq.close()

        self.info = self.im.create_text(630, 15, text="Fullscreen?", anchor=W, font=self.fontPadrao)

        self.lang = self.im.create_text(630, 65, text="Language", anchor=W, font=self.fontPadrao)

        full = Button(text="On", font=self.fontPadrao, width=9)
        if config[0][:-1] == 'fullscreen':
            full['fg'] = 'white'
            full['bg'] = 'gray'
        else:
            full['command'] = self.full
        self.fullb = self.im.create_window(580, 40, window=full, anchor=W)

        max1 = Button(text="Off", font=self.fontPadrao, width=9)
        if config[0][:-1] == 'zoomed':
            max1['fg'] = 'white'
            max1['bg'] = 'gray'
        else:
            max1['command'] = self.max
        self.maxb = self.im.create_window(670, 40, window=max1, anchor=W)

        pt = Button(text="PT", font=self.fontPadrao, width=6)
        if config[1][:-1] == 'PT':
            pt['fg'] = 'white'
            pt['bg'] = 'gray'
        else:
            pt['command'] = self.pt
        self.ptb = self.im.create_window(580, 90, window=pt, anchor=W)

        en = Button(text="EN", font=self.fontPadrao, width=6)
        if config[1][:-1] == 'EN':
            en['fg'] = 'white'
            en['bg'] = 'gray'
        else:
            en['command'] = self.en
        self.enb = self.im.create_window(640, 90, window=en, anchor=W)

        jp = Button(text="JP", font=self.fontPadrao, width=6)
        if True:
            jp['fg'] = 'white'
            jp['bg'] = 'gray'
        else:
            en['command'] = self.jp
        self.jpb = self.im.create_window(700, 90, window=jp, anchor=W)

        x = {'PT': 'Voltar', 'EN': 'Back'}[self.idioma]
        voltar = Button(text=x, font=self.fontPadrao, width=20, command=self.menu)
        self.voltar = self.im.create_window(580, 190, window=voltar, anchor=W)

    def full(self):

        self.im.delete(self.info, self.fullb, self.maxb, self.ptb, self.enb, self.jpb, self.voltar)
        self.app.attributes('-fullscreen', True)
        arq = open('config.svtg', 'r')
        x = arq.readlines()
        x[0] = 'fullscreen\n'
        arq = open('config.svtg', 'w')
        arq.writelines(x)
        arq.close()
        OP(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def max(self):

        self.im.delete(self.info, self.fullb, self.maxb, self.ptb, self.enb, self.jpb, self.voltar)
        self.app.attributes('-fullscreen', False)
        self.app.state("zoomed")
        arq = open('config.svtg', 'r')
        x = arq.readlines()
        x[0] = 'zoomed\n'
        arq = open('config.svtg', 'w')
        arq.writelines(x)
        arq.close()
        OP(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def pt(self):

        self.idioma = 'PT'
        self.im.delete(self.info, self.fullb, self.maxb, self.ptb, self.enb, self.jpb, self.voltar)
        arq = open('config.svtg', 'r')
        x = arq.readlines()
        x[1] = 'PT\n'
        arq = open('config.svtg', 'w')
        arq.writelines(x)
        arq.close()
        OP(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def en(self):

        self.idioma = 'EN'
        self.im.delete(self.info, self.fullb, self.maxb, self.ptb, self.enb, self.jpb, self.voltar)
        arq = open('config.svtg', 'r')
        x = arq.readlines()
        x[1] = 'EN\n'
        arq = open('config.svtg', 'w')
        arq.writelines(x)
        arq.close()
        OP(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def menu(self):

        self.im.delete(self.info, self.fullb, self.maxb, self.ptb, self.enb, self.jpb, self.voltar)
        Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)
