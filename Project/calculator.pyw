from graphics import *

#Set window and coords
win = GraphWin("Calculator",300,400)
win.setCoords(0.0,0.0,22,27)

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

acc = Rectangle(Point(1, 26),Point(21, 22))
acc.setFill('LightGreen')
acc.draw(win)
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
           [memSubstitute,'MS'],[Clear,'Clear'],[num7,'7'],[num4,'4'],[num1,'1'],
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
        for var,txt in buttontxt:
            if var.getP1().getX() < click.getX() < var.getP2().getX()\
               and var.getP1().getY() > click.getY() > var.getP2().getY():
                return txt

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
