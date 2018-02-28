#Caluclator.py
#Caluclator project
from graphics import *

##Creating the graphics for the calculator

win = GraphWin("Calculator",300,400)
win.setCoords(0.0,0.0,30.0,30.0)

#accumulator
accp1,accp2,accp3 = Point(2.0, 29.0), Point(28.0, 25.0), Point(2.0,25.0)
acc = Rectangle(accp1,accp2)

accwidth = accp2.getX() - accp1.getX()

acc.draw(win)

buttonwidth = accwidth / 4


#Number row 1

pC1 = Point(accp3.getX(), accp3.getY() - 1.25)
pC2 = Point(pC1.getX() + buttonwidth,pC1.getY() - buttonwidth + 2)
Clear = Rectangle(pC1,pC2)

Clear.draw(win)

p71 = Point(pC1.getX(), pC1.getY() - buttonwidth + 2)
p72 = Point(pC2.getX(), pC2.getY() - buttonwidth + 2)
num7 = Rectangle(p71,p72)

num7.draw(win)

p41 = Point(p71.getX(), p71.getY() - buttonwidth + 2)
p42 = Point(p72.getX(), p72.getY() - buttonwidth + 2)
num4 = Rectangle(p41,p42)

num4.draw(win)

p11 = Point(p41.getX(), p41.getY() - buttonwidth + 2)
p12 = Point(p42.getX(), p42.getY() - buttonwidth + 2)
num1 = Rectangle(p11,p12)

num1.draw(win)

p01 = Point(p11.getX(), p11.getY() - buttonwidth + 2)
p02 = Point(p12.getX() + buttonwidth, p12.getY() - buttonwidth + 2)
num0 = Rectangle(p01,p02)

txt0 = Text(Point(p12.getX(), p12.getY() - buttonwidth / 2 + 1), "0")
txt0.draw(win)

num0.draw(win)


#Number row 2

pNeg1 = Point(pC1.getX() + buttonwidth, pC1.getY())
pNeg2 = Point(pC2.getX() + buttonwidth, pC2.getY())
numNeg = Rectangle(pNeg1,pNeg2)

numNeg.draw(win)

p81 = Point(pNeg1.getX(), pNeg1.getY() - buttonwidth + 2)
p82 = Point(pNeg2.getX(), pNeg2.getY() - buttonwidth + 2)
num8 = Rectangle(p81,p82)

num8.draw(win)

p51 = Point(p81.getX(), p81.getY() - buttonwidth + 2)
p52 = Point(p82.getX(), p82.getY() - buttonwidth + 2)
num5 = Rectangle(p51,p52)

num5.draw(win)

p21 = Point(p51.getX(), p51.getY() - buttonwidth + 2)
p22 = Point(p52.getX(), p52.getY() - buttonwidth + 2)
num2 = Rectangle(p21,p22)

num2.draw(win)


#Number row 3

pPrecent1 = Point(pC1.getX() + buttonwidth * 2, pC1.getY())
pPrecent2 = Point(pC2.getX() + buttonwidth * 2, pC2.getY())
numPrecent = Rectangle(pPrecent1,pPrecent2)

numPrecent.draw(win)


p91 = Point(pPrecent1.getX(), pPrecent1.getY() - buttonwidth + 2)
p92 = Point(pPrecent2.getX(), pPrecent2.getY() - buttonwidth + 2)
num9 = Rectangle(p91,p92)

num9.draw(win)

p61 = Point(p91.getX(), p91.getY() - buttonwidth + 2)
p62 = Point(p92.getX(), p92.getY() - buttonwidth + 2)
num6 = Rectangle(p61,p62)

num6.draw(win)

p31 = Point(p61.getX(), p61.getY() - buttonwidth + 2)
p32 = Point(p62.getX(), p62.getY() - buttonwidth + 2)
num3 = Rectangle(p31,p32)

num3.draw(win)


pp1 = Point(p31.getX(), p31.getY() - buttonwidth + 2)
pp2 = Point(p32.getX(), p32.getY() - buttonwidth + 2)
pp = Rectangle(pp1,pp2)

pp.draw(win)


#Row 4

devide1 = Point(pC1.getX() + buttonwidth * 3, pC1.getY())
devide2 = Point(pC2.getX() + buttonwidth * 3, pC2.getY())
devide = Rectangle(devide1,devide2)

devide.draw(win)


mult1 = Point(devide1.getX(), devide1.getY() - buttonwidth + 2)
mult2 = Point(devide2.getX(), devide2.getY() - buttonwidth + 2)
mult = Rectangle(mult1,mult2)

mult.draw(win)

sub1 = Point(mult1.getX(), mult1.getY() - buttonwidth + 2)
sub2 = Point(mult2.getX(), mult2.getY() - buttonwidth + 2)
sub = Rectangle(sub1,sub2)

sub.draw(win)

add1 = Point(sub1.getX(), sub1.getY() - buttonwidth + 2)
add2 = Point(sub2.getX(), sub2.getY() - buttonwidth + 2)
add = Rectangle(add1,add2)

add.draw(win)


equal1 = Point(add1.getX(), add1.getY() - buttonwidth + 2)
equal2 = Point(add2.getX(), add2.getY() - buttonwidth + 2)
equal = Rectangle(equal1,equal2)

equal.draw(win)
