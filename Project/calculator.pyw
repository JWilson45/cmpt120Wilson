from graphics import *

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
num01 = buttonCreation(num1)
num0 = Rectangle(num01.getP1(),Point(num01.getP2().getX()+4,
                                     num01.getP2().getY())) 
#5
changeSign = buttonShift(Clear)
num8 = buttonCreation(changeSign)
num5 = buttonCreation(num8)
num2 = buttonCreation(num5)
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
           ,[num0,'0'],[changeSign,'+ / -'],[num8,'8'],[num5,'5'],[num2,'2'],
           [percent,'%'],[num9,'9'],[num6,'6'],[num3,'3'],[point,'.'],
           [divide,'/'],[mult,'x'],[sub,'-'],[add,'+'],[equal,'='],
           [sqrRoot,'√'],[square,'x^2'],[_1overX,'1/x'],[Popen,'('],[Pclose,')']
           ]
#make this work
scientxt = [[sin,'sin'],[cos,'cos'],[tan,'tan'],[sin1,'sin-1'],[cos1,'cos-1'],
            [tan1,'tan-1'],[log,'log'],[ln,'ln'],[xY,'x^y'],[tenX,'10^x']]

for var,txt in buttontxt:
    text = Text(var.getCenter(),txt)
    var.draw(win)
    text.draw(win)

for var,txt in scientxt:
    text = Text(var.getCenter(),txt)
    var.draw(win)
    text.draw(win)

#Get click
def getclick():
    while 1 == 1:
        click = win.getMouse()
        for var,txt in buttontxt:
            if var.getP1().getX() < click.getX() < var.getP2().getX()\
               and var.getP1().getY() > click.getY() > var.getP2().getY():
                return txt
        for var,txt in scientxt:
            if var.getP1().getX() < click.getX() < var.getP2().getX()\
               and var.getP1().getY() > click.getY() > var.getP2().getY():
                return txt

from calc_functions import *

def main():
    display,displaypoint,mem,calculateList = '',acc.getCenter(),'0',['']
    displayElement, memoryElement = Text(displaypoint, display), Text(memP, mem)
    listnum = 0      
    while 1 == 1:
        symbol = getclick()
#Equals
        if symbol == '=':
            try:
                display = evaluate(calculateList)
                calculateList = [display]
                listnum = 0
            except:
                print('Excpet catch error')
                pass
                
            
#Operators
        elif symbol == '+' or symbol == '-' or symbol == '/' or symbol == 'x'\
             or symbol == '(' or symbol == ')':
            if symbol == 'x':
                symbol = '*'
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
             or symbol == 'ln' or symbol == 'x^y' or symbol == '10^x':
            calculateList[listnum] = special(calculateList[listnum],symbol)
            display = displaySet(calculateList)
#Memory
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
            if symbol != 'MC':
                memlen = len(mem)
                memoryElement = Text(Point(memP.getX()+(memlen*.23),
                                           memP.getY()),'Memory: ' + mem)
                memoryElement.draw(win)
            display = displaySet(calculateList)
#Clear
        elif symbol == 'Clear' or display == 'Error':
            display,calculateList,listnum = reset()
#Numbers
        else:
            calculateList[listnum] = calculateList[listnum] + symbol
            display = displaySet(calculateList)
        displayElement.undraw() 
        displayElement = Text(displaypoint,display)
        displayElement.draw(win)

main()
