import tkinter as tk
from Vsaves import VerificadorSaves
import Menu_Inicial


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

        im = tk.Canvas(app, width=2000, height=1100)
        imagem = tk.PhotoImage(file="img\\1.png")
        painel = im.create_image(0, 0, image=imagem, anchor=tk.NW)
        im.lower(painel)
        im.pack()
        im.image = imagem

        Menu_Inicial.Inicio(im, idioma, app, fonte_padrao)


VerificadorSaves()
root = tk.Tk()
DungeonNeedI(root)
root.mainloop()
