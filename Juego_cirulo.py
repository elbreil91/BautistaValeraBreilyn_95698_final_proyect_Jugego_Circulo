from graphics import *
from random import *
import datetime


class Juego_Circulo:

    def __init__(self):
        self.win = GraphWin('Golpea al topo',400,400)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground(color_rgb(176,146,111))



    def topo(self):
        for x in range(10):
            cir = Circle(Point(10,10),5)
            cir.setOutline('blue')
            cir.setWidth(2)
            cir.draw(self.win)
            cir.move(randint(0,80),randint(0,80))
        return cir


    def cloucid(self):
        key = self.win.getKey()

        if key == "q":
            self.win.close()





def main():
    game = Juego_Circulo()
    game.topo()
    game.cloucid()


if __name__ =="__main__":
    main()




