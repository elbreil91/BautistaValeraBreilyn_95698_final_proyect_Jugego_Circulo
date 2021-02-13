from graphics import *
from random import *
import datetime


class Juego_Circulo:

    def __init__(self):
        self.win = GraphWin('Golpea al topo',400,400)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground(color_rgb(176,146,111))
        self.win.getMouse()
        self.win.close()










game = Juego_Circulo()
game.run()



