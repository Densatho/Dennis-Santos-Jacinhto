import os
import ctypes


class VerificadorSaves:

    def __init__(self):

        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        try:
            open("saves\\Slot 1.svt", 'r')
        except FileNotFoundError:
            os.system("mkdir saves")
            
        try:
            open("saves\\Slot 1.svt", 'r')
        except IOError:
            arq = open('saves\\Slot 1.svt', 'w')
            arq.close()

        try:
            open("saves\\Slot 2.svt", 'r')
        except IOError:
            arq = open('saves\\Slot 2.svt', 'w')
            arq.close()
        try:
            open("saves\\Slot 3.svt", 'r')
        except IOError:
            arq = open('saves\\Slot 3.svt', 'w')
            arq.close()
        try:
            open("saves\\Slot 4.svt", 'r')
        except IOError:
            arq = open('saves\\Slot 4.svt', 'w')
            arq.close()
        try:
            open("saves\\Slot 5.svt", 'r')
        except IOError:
            arq = open('saves\\Slot 5.svt', 'w')
            arq.close()

        try:
            open("config.svtg", 'r')
        except IOError:
            arq = open('config.svtg', 'w')
            txt = ['fullscreen\n', 'EN\n', f'{screensize[0]}\n', f'{screensize[1]}\n']
            arq.writelines(txt)
            arq.close()
