from graphics import *

#Set window and coords
win = GraphWin("Calculator",450,425)
win.setCoords(0,0,34,27)

def buttonCreation(pre):
    new = Rectangle(Point(pre.getP1().getX(),pre.getP1().getY() - 4),
                    Point(pre.getP2().getX(),pre.getP2().getY() - 4))
    return new

def buttonShift(shift):
    new = Rectangle(Point(shift.getP1().getX() + 4,shift.getP1().getY()),
                    Point(shift.getP2().getX() + 4,shift.getP2().getY()))
    return new

acc,memP = Rectangle(Point(1, 26),Point(33, 22)),Point(3.5, 25)
acc.setFill('LightGreen')
acc.draw(win)
displaySci = Text(Point(memP.getX()+.5,memP.getY() -2.5),'Scientific Mode')
btxt = [
    ['sin','sin-1','MC','Clear','+ / -','%','/','√'],
    ['cos','cos-1','M+','7','8','9','x','x^2'],
    ['tan','tan-1','M-','4','5','6','-','1/x'],
    ['log','ln','MR','1','2','3','+','x^y'],
    ['(',')','MS','Scientific \n Mode','0','.','=','10^x']
    ]
buttonDict = {'begin': Rectangle(Point(-3.0, 25.0), Point(1.0, 21.0))}
for i in range(5):
    buttonDict['begin'],prev = buttonCreation(buttonDict['begin']),'begin'
    for j in range(8):
        sym = btxt[i][j]
        buttonDict[sym] = buttonShift(buttonDict[prev])
        prev,text = sym, Text(buttonDict[sym].getCenter(),sym)
        buttonDict[sym].draw(win)
        text.draw(win)

def draw():
    block1.draw(win)
    block2.draw(win)
    
block1 = Rectangle(buttonDict['sin'].getP1(),buttonDict['ln'].getP2())
block2 = Rectangle(buttonDict['x^y'].getP1(),buttonDict['10^x'].getP2())
block1.setFill('White')
block2.setFill('White')
draw()

#Get click
def getclick(sci):
    while 1 == 1:
        click = win.getMouse()
        if not sci and (1 < click.getX() < 9 and 21 > click.getY() > 5 or
                        28 < click.getX() < 32 and 9 > click.getY() > 1):
            continue
        for txt,var in buttonDict.items():
            if var.getP1().getX() < click.getX() < var.getP2().getX()\
               and var.getP1().getY() > click.getY() > var.getP2().getY():
                return txt

def sciMode(sci):
    if sci:
        sci = False
        draw()
        displaySci.undraw()
    elif not sci:
        sci = True
        block1.undraw()
        block2.undraw()
        displaySci.draw(win)
    return sci

from calc_functions import *

def main():
#set varriables
    centeracc = acc.getCenter()
    display,displaypoint = '',Point(centeracc.getX(),centeracc.getY()+.20)
    calculateList,mem,display2 = [''],'0',''
    displaypointans = Point(centeracc.getX(), centeracc.getY()-.80)
    displayElement, memoryElement = Text(displaypoint, display), Text(memP, mem)
    displayElementAns,listnum,sci = Text(displaypointans,display2), 0, False
    displayElement.draw(win)
    displayElementAns.draw(win)
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
            except: continue
#Operators
        elif symbol == '+' or symbol == '-' or symbol == '/' or symbol == 'x'\
             or symbol == '(' or symbol == ')' or symbol == 'x^y':
            calculateList, symbol = operatortest(symbol,display2,calculateList,display)
            calculateList,listnum = append(calculateList,listnum)
            calculateList[listnum] = calculateList[listnum] + symbol
            calculateList,listnum = append(calculateList,listnum)
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
                    mem = memory(symbol,display2,mem)
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
#Scientific Mode
        elif symbol == 'Scientific \n Mode':
            sci = sciMode(sci)
            continue
#Numbers
        else:
            calculateList[listnum] = calculateList[listnum] + symbol
            display = displaySet(calculateList)
            display2 = symbol
        displayElement.setText(display)
        displayElementAns.setText(display2)

main()
