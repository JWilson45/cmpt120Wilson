from graphics import *

#Set window and coords
win = GraphWin("Calculator",350,400)
win.setCoords(0.0,0.0,26,27)

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

acc = Rectangle(Point(1, 26),Point(25, 22))
acc.setFill('LightGreen')
acc.draw(win)
memP = Point(acc.getP1().getX() + 2.5,acc.getP1().getY() - 1)
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
#6
sqrRoot = buttonShift(divide)
square = buttonCreation(sqrRoot)
_1overX = buttonCreation(square)
blank1=buttonCreation(_1overX)
blank2=buttonCreation(blank1)

#Text
buttontxt=[[memC,'MC'],[memAdd,'M+'],[memSubtract,'M-'],[memRecall,'MR'],
           [memSubstitute,'MS'],[Clear,'Clear'],[num7,'7'],[num4,'4'],[num1,'1']
           ,[num0,'0'],[changeSign,'+ / -'],[num8,'8'],[num5,'5'],[num2,'2'],
           [percent,'%'],[num9,'9'],[num6,'6'],[num3,'3'],[point,'.'],
           [divide,'/'],[mult,'x'],[sub,'-'],[add,'+'],[equal,'='],
           [sqrRoot,'√'],[square,'x^2'],[_1overX,'1/x'],[blank1,''],[blank2,'']]

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
    display,displaypoint,mem = '', acc.getCenter(), '0'
    displayElement = Text(displaypoint, display)
    memoryElement = Text(memP, mem)
    calculateList = ['','','']
    listnum = 0
    while 1 == 1:
        symbol = getclick()
        if symbol == '=':
            display = determine(calculateList)
            if display[-2:] == '.0':
                display = display[:-2]
            calculateList = [display, '' , '']
            listnum = 0
        elif symbol == '+' or symbol == '-' or symbol == '/' or symbol == 'x':
            listnum = listnum + 1
            calculateList[listnum] = calculateList[listnum] + symbol
            listnum = listnum + 1
            display = calculateList[0] + calculateList[1] + calculateList[2]
        elif symbol == '√' or symbol == 'x^2' or symbol == '1/x'\
             or symbol == '+ / -' or symbol == '%':
            calculateList[listnum] = special(calculateList[listnum],symbol)
            display = calculateList[0] + calculateList[1] + calculateList[2]
        elif symbol == 'MC' or symbol == 'M+' or symbol == 'M-' \
             or symbol == 'MR' or symbol == 'MS':
            if symbol == 'MC':
                mem = '0'
            elif symbol == 'MR':
                calculateList[listnum] = mem
            elif symbol == 'MS':
                mem = calculateList[listnum]
            else: mem = memory(symbol,calculateList[listnum],mem)
            memoryElement.undraw()
            memoryElement = Text(memP, 'Memory: ' + mem)
            if symbol != 'MC':
                memoryElement.draw(win)
            display = calculateList[0] + calculateList[1] + calculateList[2]
        elif symbol == 'Clear':
            display = ''
            calculateList = ['','','']
            listnum = 0
            display = calculateList[0] + calculateList[1] + calculateList[2]
        else:
            calculateList[listnum] = calculateList[listnum] + symbol
            display = calculateList[0] + calculateList[1] + calculateList[2]
        displayElement.undraw() 
        displayElement = Text(displaypoint,display)
        displayElement.draw(win)
        if display == 'Error':
            win.getMouse()
            display = ''
            calculateList = ['','','']
            listnum = 0

main()
