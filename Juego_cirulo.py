from graphics import *
from random import *
import datetime




def main():
    w,h = 500,500
    win = GraphWin('juego',w,h,autoflush=False)
    win.setCoords(0,0,100,100)
    p1,p2,rad = 15,15,5
    intru = Text(Point(35,97),'Haga clik para en pesar y "q" + clik para salir.')
    intru.setFill('blue')
    intru.draw(win)





    while True:
        key = win.checkKey()
        if key == 'q':
            break

        circulo = Circle(Point(p1, p2), rad)
        circulo.setOutline('blue')
        circulo.setWidth(2)
        centro = circulo.getCenter()
        if centro != w and h:
            circulo.move(randint(0, 80), randint(0, 70))
            circulo.draw(win)


        shape = Circle(Point(0, 0), 4)
        cie = win.getMouse()
        cu = shape.getCenter()
        rectx = cie.getX() - cu.getX()
        recty = cie.getY() - cu.getY()
        shape.setFill('green')
        mov = shape.move(rectx, recty)
        shape.draw(win)
        update(4 / 4)
        n = 60
        secs = datetime.datetime.now()
        tim = 60 - secs.second
        te = Text(Point(98,98),tim)
        te.draw(win)
        update(4)
        te.undraw()
        

        circulo.undraw()
        update(4)
        shape.undraw()

    win.close()
main()








