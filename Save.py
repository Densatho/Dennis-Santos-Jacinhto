from tkinter import *
from FBase import *
import Menu


class Save:

    def __init__(self, im, idioma, app, fontpadrao, p, mp):

        self.im = im
        self.idioma = idioma
        self.app = app
        self.fontPadrao = fontpadrao
        self.p = p
        self.mp = mp

        x = {'PT': "Selecione o Slot que deseja salvar:", 'EN': 'Select a Slot to Save'}[self.idioma]
        self.info = self.im.create_text({'PT': 550, 'EN': 600}[self.idioma], 15, text=x, anchor=W, font=self.fontPadrao)

        arq = open('saves\\Slot 1.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot1 = Button(text='Slot 1 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot1s)
        self.slot1 = self.im.create_window(580, 40, window=slot1, anchor=W)

        arq = open('saves\\Slot 2.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot2 = Button(text='Slot 2 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot2s)
        self.slot2 = self.im.create_window(580, 70, window=slot2, anchor=W)

        arq = open('saves\\Slot 3.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot3 = Button(text='Slot 3 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot3s)
        self.slot3 = self.im.create_window(580, 100, window=slot3, anchor=W)

        arq = open('saves\\Slot 4.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot4 = Button(text='Slot 4 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot4s)
        self.slot4 = self.im.create_window(580, 130, window=slot4, anchor=W)

        arq = open('saves\\Slot 5.svt', 'r')
        aux = arq.readlines()
        if len(aux) > 2:
            auxn, auxa = aux[10][0:-1].split('-')
            nome = aux[0][0:-1] + ' nv' + auxn
        else:
            nome = 'Empty'
        slot5 = Button(text='Slot 5 - {}'.format(nome), font=self.fontPadrao, width=20, command=self.slot5s)
        self.slot5 = self.im.create_window(580, 160, window=slot5, anchor=W)
        arq.close()

        x = {'PT': "Voltar", 'EN': 'Back'}[self.idioma]
        sair = Button(text=x, font=self.fontPadrao, width=20)
        sair["command"] = self.menu
        self.sair = self.im.create_window(580, 190, window=sair, anchor=W)

        self.aux = 0

    def menu(self):

        self.im.delete(self.info, self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.sair)
        Menu.Menu(self.im, self.idioma, self.app, self.fontPadrao, self.p, self.mp)

    def slot1s(self):

        self.aux = 'saves\\Slot 1.svt'
        self.salvar()

    def slot2s(self):

        self.aux = 'saves\\Slot 2.svt'
        self.salvar()

    def slot3s(self):

        self.aux = 'saves\\Slot 3.svt'
        self.salvar()

    def slot4s(self):

        self.aux = 'saves\\Slot 4.svt'
        self.salvar()

    def slot5s(self):

        self.aux = 'saves\\Slot 5.svt'
        self.salvar()

    def salvar(self):
                
        arq = open(self.aux, 'w')
        del self.aux
        arq.writelines(self.p[0]+'\n')
        arq.writelines(str(self.p[1].vida)+'\n')
        arq.writelines(str(self.p[1].vida_m)+'\n')
        arq.writelines(str(self.p[1].m)+'\n')
        arq.writelines(str(self.p[1].mm)+'\n')
        arq.writelines(str(self.p[1].d)+'\n')
        arq.writelines(str(self.p[1].i)+'\n')
        arq.writelines(str(self.p[1].t)+'\n')
        arq.writelines(str(self.p[1].s)+'\n')
        arq.writelines(str(self.p[1].r)+'\n')
        arq.writelines(str(self.p[2][0])+'-'+str(self.p[2][1])+'\n')
        arq.writelines(str(self.p[3])+'\n')
        arq.writelines(str(self.p[4])+'\n')
        arq.writelines(str(self.mp)+'\n')
        for i in range(0, len(self.p[5])):
            arq.writelines(str(self.p[5][i].nome) + '\n')
        arq.close()

        self.im.delete(self.info, self.slot1, self.slot2, self.slot3, self.slot4, self.slot5, self.sair)
        self.menu()
