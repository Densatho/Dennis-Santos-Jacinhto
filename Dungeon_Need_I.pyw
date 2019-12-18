import tkinter as tk
from Vsaves import VerificadorSaves
import Menu_Inicial
from PIL import Image


class DungeonNeedI:

    def __init__(self, app):

        app.title("Dungeon Need I")
        arq = open('config.svtg', 'r')
        config = arq.readlines()

        if config[0][:-1] == 'fullscreen':
            app.attributes('-fullscreen', True)
        else:
            app.state("zoomed")
        arq.close()
        idioma = config[1][:-1]

        fonte_padrao = ("Arial", "10", "bold")

        im = tk.Canvas(app, width=config[2][:-1], height=config[3][:-1])
        imagem = Image.open("img\\1.png")
        imagem = imagem.resize((int(config[2][:-1]), int(config[3][:-1])), Image.ANTIALIAS)
        imagem.save("img\\1re.ppm")
        imagem = tk.PhotoImage(file="img\\1re.ppm")
        painel = im.create_image(0, 0, image=imagem, anchor=tk.NW)
        im.lower(painel)
        im.pack()
        im.image = imagem

        Menu_Inicial.Inicio(im, idioma, app, fonte_padrao)


VerificadorSaves()
root = tk.Tk()
DungeonNeedI(root)
root.mainloop()
