from graphics import *

# JA: You could simplify your code with some functions

#Set window and coords
win = GraphWin("Calculator",450,425)
win.setCoords(0,0,34,27)

def buttonCreation(perviousRect):
    new = Rectangle(Point(perviousRect.getP1().getX(),
                          perviousRect.getP1().getY() - 4),
                    Point(perviousRect.getP2().getX(),
                          perviousRect.getP2().getY() - 4))
    return new

def buttonShift(rectShift):
    new = Rectangle(Point(rectShift.getP1().getX() + 4,
                          rectShift.getP1().getY()),
                    Point(rectShift.getP2().getX() + 4,
                          rectShift.getP2().getY()))
    return new

acc = Rectangle(Point(1, 26),Point(33, 22))
acc.setFill('LightGreen')
acc.draw(win)
memP = Point(acc.getP1().getX() + 2.5,acc.getP1().getY() - 1)
startRect = Rectangle(Point(acc.getP1().getX(),acc.getP1().getY()-5),
                      Point(acc.getP1().getX()+4,acc.getP1().getY()-9))
#1
sin = startRect
cos = buttonCreation(sin)
tan = buttonCreation(cos)
log = buttonCreation(tan)
Popen = buttonCreation(log)
#2
sin1 = buttonShift(sin)
cos1 = buttonCreation(sin1)
tan1 = buttonCreation(cos1)
ln = buttonCreation(tan1)
Pclose =buttonShift(Popen)
#3    
memC = buttonShift(sin1)
memAdd = buttonCreation(memC)
memSubtract = buttonCreation(memAdd)
memRecall = buttonCreation(memSubtract)
memSubstitute = buttonCreation(memRecall)
#4
Clear = buttonShift(memC)
num7 = buttonCreation(Clear)
num4 = buttonCreation(num7)
num1 = buttonCreation(num4)
sciMode = buttonCreation(num1)
#5
changeSign = buttonShift(Clear)
num8 = buttonCreation(changeSign)
num5 = buttonCreation(num8)
num2 = buttonCreation(num5)
num0 = buttonCreation(num2)
#6
percent = buttonShift(changeSign)
num9 = buttonCreation(percent)
num6 = buttonCreation(num9)
num3 = buttonCreation(num6)
point = buttonCreation(num3)
#7
divide = buttonShift(percent)
mult = buttonCreation(divide)
sub = buttonCreation(mult)
add = buttonCreation(sub)
equal = buttonCreation(add)
#8
sqrRoot = buttonShift(divide)
square = buttonCreation(sqrRoot)
_1overX = buttonCreation(square)
xY=buttonCreation(_1overX)
tenX=buttonCreation(xY)

#Text
buttontxt=[[memC,'MC'],[memAdd,'M+'],[memSubtract,'M-'],[memRecall,'MR'],
           [memSubstitute,'MS'],[Clear,'Clear'],[num7,'7'],[num4,'4'],[num1,'1']
           ,[sciMode,'Scientific \n Mode'],[num0,'0'],[changeSign,'+ / -'],
           [num8,'8'],[num5,'5'],[num2,'2'],[percent,'%'],[num9,'9'],[num6,'6'],
           [num3,'3'],[point,'.'],[divide,'/'],[mult,'x'],[sub,'-'],[add,'+'],
           [equal,'='],[sqrRoot,'√'],[square,'x^2'],[_1overX,'1/x'],
           [Popen,'('],[Pclose,')']
           ]

scientxt = [[sin,'sin'],[cos,'cos'],[tan,'tan'],[sin1,'sin-1'],[cos1,'cos-1'],
            [tan1,'tan-1'],[log,'log'],[ln,'ln'],[xY,'x^y'],[tenX,'10^x']]

block1,block2 = Rectangle(sin.getP1(),ln.getP2()),Rectangle(xY.getP1(),
                                                            tenX.getP2())
block1.setFill('White')
block2.setFill('White')
block1.draw(win)
block2.draw(win)

for var,txt in buttontxt:
    text = Text(var.getCenter(),txt)
    var.draw(win)
    text.draw(win)

##for var,txt in scientxt:
##    text = Text(var.getCenter(),txt)
##    var.draw(win)
##    text.draw(win)

#Get click
def getclick(sci):
    while 1 == 1:
        click = win.getMouse()
        for var,txt in buttontxt:
            if var.getP1().getX() < click.getX() < var.getP2().getX()\
               and var.getP1().getY() > click.getY() > var.getP2().getY():
                return txt
        if sci:
            for var,txt in scientxt:
                if var.getP1().getX() < click.getX() < var.getP2().getX()\
                   and var.getP1().getY() > click.getY() > var.getP2().getY():
                    return txt

from calc_functions import *

def main():
    centeracc = acc.getCenter()
    display,displaypoint,mem,calculateList = '',Point(centeracc.getX(),
                                                      centeracc.getY()+.20)\
                                                      ,'0',['']
    display2 = ''
    displaypointans = Point(centeracc.getX(), centeracc.getY()-.80)
    displayElement, memoryElement = Text(displaypoint, display), Text(memP, mem)
    displayElement.draw(win)
    displayElementAns = Text(displaypointans,display2)
    displayElementAns.draw(win)
    displaySci = Text(Point(memP.getX()+.5,memP.getY() -2.5),'Scientific Mode')
    listnum = 0
    sci = False
    while 1 == 1:
        symbol = getclick(sci)
#Equals
        if symbol == '=':
            try:
                display2 = evaluate(calculateList)
                display = ''
                calculateList = [display]
                listnum = 0
                displayElementAns.setText(display2)
                continue
            except:
                continue
#Scientific Mode
        elif symbol == 'Scientific \n Mode':
            if sci:
                sci = False
                for var,txt in scientxt:
                    var.undraw()
                block1.draw(win)
                block2.draw(win)
                displaySci.undraw()
            elif sci is False:
                sci = True
                for var,txt in scientxt:
                    text = Text(var.getCenter(),txt)
                    var.draw(win)
                    text.draw(win)
                block1.undraw()
                block2.undraw()
                displaySci.draw(win)
            continue
#Operators
        elif symbol == '+' or symbol == '-' or symbol == '/' or symbol == 'x'\
             or symbol == '(' or symbol == ')' or symbol == 'x^y':
            if symbol == 'x':
                symbol = '*'
            if symbol == 'x^y':
                symbol = '**'
            if display == '':
                calculateList = [display2]
            calculateList.append('')
            listnum = listnum + 1
            calculateList[listnum] = calculateList[listnum] + symbol
            calculateList.append('')
            listnum = listnum + 1
            display = displaySet(calculateList)
#Special Characters
        elif symbol == '√' or symbol == 'x^2' or symbol == '1/x'\
             or symbol == '+ / -' or symbol == '%' or symbol == 'sin'\
             or symbol == 'cos' or symbol == 'tan' or symbol == 'sin-1'\
             or symbol == 'cos-1' or symbol == 'tan-1' or symbol == 'log'\
             or symbol == 'ln' or symbol == '10^x':
            try:
                if display == '':
                    calculateList = [display2]
                calculateList[listnum] = special(calculateList[listnum],symbol)
                display = displaySet(calculateList)
            except:
                continue
#Memory
        elif symbol == 'MC' or symbol == 'M+' or symbol == 'M-' \
             or symbol == 'MR' or symbol == 'MS':
            if symbol == 'MC':
                mem = '0'
            elif symbol == 'MR':
                calculateList[listnum] = mem
            elif symbol == 'MS':
                mem = display2
            else:
                try:
                    mem = memory(symbol,calculateList[listnum],mem)
                except:
                    continue
            memoryElement.undraw()
            if symbol != 'MC':
                memlen = len(mem)
                memoryElement = Text(Point(memP.getX()+(memlen*.23),
                                           memP.getY()),'Memory: ' + mem)
                memoryElement.draw(win)
            if symbol == 'MS':
                continue
            display = displaySet(calculateList)
#Clear
        elif symbol == 'Clear' or display == 'Error':
            display,calculateList,listnum,display2 = reset()
#Numbers
        else:
            calculateList[listnum] = calculateList[listnum] + symbol
            display = displaySet(calculateList)
        displayElement.setText(display)
        displayElementAns.setText(display2)

main()
