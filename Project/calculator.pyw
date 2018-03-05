from graphics import *

##Creating the graphics for the calculator

#Set window and coords
win = GraphWin("Calculator",300,400)
win.setCoords(0.0,0.0,22,27)

#accumulator
accp1,accp2,accp3 = Point(1, 26), Point(21, 22), Point(1,22)
acc = Rectangle(accp1,accp2)
acc.setFill('LightGreen')
acc.draw(win)

def buttonCreation(perviousRect):
    new = Rectangle(Point(perviousRect.getP1().getX(),
                          perviousRect.getP1().getY() - 4),
                    Point(perviousRect.getP2().getX(),
                          perviousRect.getP2().getY() - 4))
    new.draw(win)
    return new

def buttonShift(rectShift):
    new = Rectangle(Point(rectShift.getP1().getX() + 4,
                          rectShift.getP1().getY()),
                    Point(rectShift.getP2().getX() + 4,
                          rectShift.getP2().getY()))
    new.draw(win)
    return new

#1    
memC = Rectangle(Point(1,21),Point(5,17))
memC.draw(win)
memAdd = buttonCreation(memC)
memSubtract = buttonCreation(memAdd)
memRecall = buttonCreation(memSubtract)
memSubstitute = buttonCreation(memRecall)
#2
Clear = buttonShift(memC)
num7 = buttonCreation(Clear)
num4 = buttonCreation(num7)
num1 = buttonCreation(num4)
num0 = Rectangle(Point(5,5),Point(13,1))
num0.draw(win)
#3
changeSign = buttonShift(Clear)
num8 = buttonCreation(changeSign)
num5 = buttonCreation(num8)
num2 = buttonCreation(num5)
#4
percent = buttonShift(changeSign)
num9 = buttonCreation(percent)
num6 = buttonCreation(num9)
num3 = buttonCreation(num6)
point = buttonCreation(num3)
#5
divide = buttonShift(percent)
mult = buttonCreation(divide)
sub = buttonCreation(mult)
add = buttonCreation(sub)
equal = buttonCreation(add)

#Text
buttontxt=[[memC,'MC'],[memAdd,'M+'],[memSubtract,'M-'],[memRecall,'MR'],
           [memSubstitute,'MS'],[Clear,'C'],[num7,'7'],[num4,'4'],[num1,'1'],
           [num0,'0'],[changeSign,'+ / -'],[num8,'8'],[num5,'5'],[num2,'2'],
           [percent,'%'],[num9,'9'],[num6,'6'],[num3,'3'],[point,'.'],
           [divide,'/'],[mult,'x'],[sub,'-'],[add,'+'],[equal,'=']]

for var,txt in buttontxt:
    text = Text(var.getCenter(),txt)
    text.draw(win)

#Get click
def getclick():
    while 1 == 1:
        click = win.getMouse()
        if pC1.getX() < click.getX() < pC2.getX() and pC1.getY() > click.getY() > pC2.getY():
            return 'Clear'
        if p71.getX() < click.getX() < p72.getX() and p71.getY() > click.getY() > p72.getY():
            return 7
        if p41.getX() < click.getX() < p42.getX() and p41.getY() > click.getY() > p42.getY():
            return 4
        if p11.getX() < click.getX() < p12.getX() and p11.getY() > click.getY() > p12.getY():
            return 1
        if pNeg1.getX() < click.getX() < pNeg2.getX() and pNeg1.getY() > click.getY() > pNeg2.getY():
            return '$'
        if p81.getX() < click.getX() < p82.getX() and p81.getY() > click.getY() > p82.getY():
            return 8
        if p51.getX() < click.getX() < p52.getX() and p51.getY() > click.getY() > p52.getY():
            return 5
        if p21.getX() < click.getX() < p22.getX() and p21.getY() > click.getY() > p22.getY():
            return 2
        if p01.getX() < click.getX() < p02.getX() and p01.getY() > click.getY() > p02.getY():
            return 0
        if pPrecent1.getX() < click.getX() < pPrecent2.getX() and pPrecent1.getY() > click.getY() > pPrecent2.getY():
            return '%'
        if p91.getX() < click.getX() < p92.getX() and p91.getY() > click.getY() > p92.getY():
            return 9
        if p61.getX() < click.getX() < p62.getX() and p61.getY() > click.getY() > p62.getY():
            return 6
        if p31.getX() < click.getX() < p32.getX() and p31.getY() > click.getY() > p32.getY():
            return 3
        if pp1.getX() < click.getX() < pp2.getX() and pp1.getY() > click.getY() > pp2.getY():
            return '.'
        if devide1.getX() < click.getX() < devide2.getX() and devide1.getY() > click.getY() > devide2.getY():
            return '/'
        if mult1.getX() < click.getX() < mult2.getX() and mult1.getY() > click.getY() > mult2.getY():
            return '*'
        if sub1.getX() < click.getX() < sub2.getX() and sub1.getY() > click.getY() > sub2.getY():
            return '-'
        if add1.getX() < click.getX() < add2.getX() and add1.getY() > click.getY() > add2.getY():
            return '+'
        if equal1.getX() < click.getX() < equal2.getX() and equal1.getY() > click.getY() > equal2.getY():
            return '='

from calc_functions import *

def main():
    display = ''
    displaypoint = acc.getCenter()
    displayElement = Text(displaypoint, display)
    displayElement.draw(win)
    while 1 == 1:
        while display[-1:] != '=':
            display = display + str(getclick())
            displayElement.undraw()
            displayElement = Text(displaypoint,display)
            displayElement.draw(win)
            if display[-5:] == 'Clear':
                display = ''
                displayElement.undraw()
            if display[-1:] == '%':
                displayElement.undraw()
                display = percent(display)
                displayElement = Text(displaypoint,display)
                displayElement.draw(win)
            if display[-1:] == '$':
                displayElement.undraw()
                display = changeSign(display)
                displayElement = Text(displaypoint,display)
                displayElement.draw(win)
        print(display)
        display = determine(display)
        displayElement.undraw()
        displayElement = Text(displaypoint,display)
        displayElement.draw(win)
        if display == 'Error':
            win.getMouse()
            display = ''
            
            
        
main()
    
