#Caluclator.py
#Caluclator project
from graphics import *

#Creating the graphics for the calculator

win = GraphWin("Calculator",300,400)
win.setCoords(0.0,0.0,30.0,30.0)

accp1,accp2,accp3 = Point(2.0, 29.0), Point(28.0, 25.0),Point(2.0,25.0)
acc = Rectangle(accp1,accp2)

accwidth = accp2.getX() - accp1.getX()

buttonwidth = accwidth / 4

pC1 = Point(accp3.getX(), accp3.getY() - 1.5)
pC2 = Point(pC1.getX() + buttonwidth,pC1.getY() - buttonwidth + 2)
Clear = Rectangle(pC1,pC2)

Clear.draw(win)


acc.draw(win)
