import os


class VerificadorSaves:

    def __init__(self):
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
            txt = ['fullscreen\n', 'EN\n']
            arq.writelines(txt)
            arq.close()
