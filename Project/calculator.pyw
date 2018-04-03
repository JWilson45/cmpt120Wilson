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

acc = Rectangle(Point(1, 26),Point(33, 22))
acc.setFill('LightGreen')
acc.draw(win)
memP,beginRect = Point(3.5, 25),Rectangle(Point(-3,5),Point(1,1))
displaySci = Text(Point(memP.getX()+.5,memP.getY() -2.5),'Scientific Mode')
btxt = [
    ['sin','sin-1','MC','Clear','+ / -','%','/','√'],
    ['cos','cos-1','M+','7','8','9','x','x^2'],
    ['tan','tan-1','M-','4','5','6','-','1/x'],
    ['log','ln','MR','1','2','3','+','x^y'],
    ['(',')','MS','Scientific \n Mode','0','.','=','10^x']
    ]
buttonDict = {'beginRec': Rectangle(Point(-3.0, 25.0), Point(1.0, 21.0))}
for i in range(5):
    buttonDict['beginRec'] = buttonCreation(buttonDict['beginRec'])
    prev = 'beginRec'
    for j in range(8):
        sym = btxt[i][j]
        buttonDict[sym] = buttonShift(buttonDict[prev])
        prev = sym
        text = Text(buttonDict[sym].getCenter(),sym)
        buttonDict[sym].draw(win)
        text.draw(win)

##block1,block2 = Rectangle(sin.getP1(),ln.getP2()),Rectangle(xY.getP1(),
##                                                            tenX.getP2())
##block1.setFill('White')
##block2.setFill('White')
##block1.draw(win)
##block2.draw(win)

#Get click
def getclick(sci):
    while 1 == 1:
        click = win.getMouse()
        for txt,var in buttonDict.items():
            if var.getP1().getX() < click.getX() < var.getP2().getX()\
               and var.getP1().getY() > click.getY() > var.getP2().getY():
                return txt
        if sci:
            for var,txt in scientxt:
                if var.getP1().getX() < click.getX() < var.getP2().getX()\
                   and var.getP1().getY() > click.getY() > var.getP2().getY():
                    return txt

def sciMode(sci):
    if sci:
        sci = False
        for var,txt in scientxt:
            var.undraw()
        block1.draw(win)
        block2.draw(win)
        displaySci.undraw()
    elif not sci:
        sci = True
        for var,txt in scientxt:
            text = Text(var.getCenter(),txt)
            var.draw(win)
            text.draw(win)
        block1.undraw()
        block2.undraw()
        displaySci.draw(win)
    return sci

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
            sci = sciMode(sci)
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
