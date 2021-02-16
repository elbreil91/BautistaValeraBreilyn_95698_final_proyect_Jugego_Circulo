from graphics import *
from random import *
from time import *
import datetime


class Juego_Circulo:

    def __init__(self):
        self.win = GraphWin('Golpea al topo',400,400)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground('green3')

    def topo(self):
        keyt = 1
        while keyt<=5:
            keyt = keyt + 1

            cir = Circle(Point(10,10),5)
            cir.setOutline('blue')
            cir.setWidth(2)
            cen = cir.getCenter()
            cir.move(randint(0,80),randint(0,80))
            update(4)
            cir.draw(self.win)
            update(4/3)
            cir.undraw()



    def Martillo(self):
        t = 1
        while t <= 5:
            t = t + 1
            shape = Circle(Point(0, 0), 4)
            cie = self.win.getMouse()
            cu = shape.getCenter()
            rectx = cie.getX() - cu.getX()
            recty = cie.getY() - cu.getY()
            shape.setFill('green')
            mov = shape.move(rectx, recty)
            update(4)
            shape.draw(self.win)
            update(4/3)
            shape.undraw()




    def cloucid(self):
        key = self.win.getKey()

        if key == "q":
            self.win.close()



def main():

    game = Juego_Circulo()
    
    game.topo()
    game.Martillo()
    game.cloucid()

if __name__ =="__main__":
    main()




