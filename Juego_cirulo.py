from graphics import *
from random import *
import datetime

class Juego_Circulo:

    def __init__(self):
        self.win = GraphWin('Golpea al topo',500,400)
        self.win.setCoords(0,0,100,100)
        self.win.setBackground('green3')


    def label(self):
        tex = Text(Point(40,95),'Aga clik para "PLAY" y "q + clik" para salir')
        tex.setFill('yellow2')
        tex.setSize(13)
        tex.setStyle("italic")
        tex.draw(self.win)

    def topo(self):
        while True:
            key = self.win.checkKey()
            if key == 'q':
                break

            circulo = Circle(Point(10, 10), 5)
            circulo.setOutline('blue')
            circulo.setWidth(2)
            centro = circulo.getCenter()
            if centro != self.win.getWidth() and self.win.getHeight():
                circulo.move(randint(0, 70), randint(0, 70))
                circulo.draw(self.win)
                update(30)

            shape = Circle(Point(0, 0), 4)
            cie = self.win.getMouse()
            cu = shape.getCenter()
            rectx = cie.getX() - cu.getX()
            recty = cie.getY() - cu.getY()
            shape.setFill('red')
            mov = shape.move(rectx, recty)
            shape.draw(self.win)
            update(30)
            n = 60
            secs = datetime.datetime.now()
            tim = 60 - secs.second
            te = Text(Point(98, 98), secs.second - 60)
            te.draw(self.win)
            update(4)
            te.undraw()

            circulo.undraw()
            update(20)
            shape.undraw()


    def cloucid(self):
        key = self.win.checkKey()

        if key == "q":
            self.win.isClosed()



def main():

    game = Juego_Circulo()
    game.label()
    game.topo()



    game.cloucid()

if __name__ =="__main__":
    main()




