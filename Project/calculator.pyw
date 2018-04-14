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
    calculateList,mem,display2 = [['']],'0',''
    displaypointans = Point(centeracc.getX(), centeracc.getY()-.80)
    displayElement, memoryElement = Text(displaypoint, display), Text(memP, mem)
    displayElementAns,sci = Text(displaypointans,display2), False
    displayElement.draw(win)
    displayElementAns.draw(win)
    listnum,listnum2 = 0,0
    prevResult = 0
    prevSymbol = ''
    while 1 == 1:
        symbol = getclick(sci)
        print(symbol)
#Clear
        if symbol == 'Clear' or display == 'Error':
            display,calculateList,listnum,listnum2,display2 = reset()
            displayElement.setText(display)
#Equals
        elif symbol == '=':
            try:
                display2 = evaluate(calculateList,listnum)
                displayElementAns.setText(display2)
                prevResult = display2
                display,calculateList,listnum,listnum2,display2 = reset()
                display = ''
                displayElement.setText(display)
                continue
            except: continue
#Parenthesis
        elif symbol == '(' or symbol == ')':
            if symbol == '(':
                calculateList.append(['('])
                prevSymbol = '('
                listnum2 = 0
            elif symbol == ')':
                print(listnum,listnum2)
                prevSymbol = ')'
                try:
                    calculateList[listnum].append(')')
                    display2 = eval(''.join(calculateList[listnum]))
                except:
                    try:
                        del calculateList[listnum]
                    except:
                        display = 'Error'
                        displayElement.setText(display)
                        displayElementAns.setText(display)
                        continue
                    continue
                calculateList.append([])
                listnum2 = -1
            display = display + symbol
            displayElement.setText(display)
            listnum += 1
            calculateList,listnum,listnum2 = append(calculateList,listnum,listnum2)
#Operators
        elif symbol == '+' or symbol == '-' or symbol == '/' or symbol == 'x'\
             or symbol == 'x^y':
            calculateList, symbol, display = operatortest(symbol,prevResult,calculateList,display)
            calculateList,listnum,listnum2 = append(calculateList,listnum,listnum2)
            calculateList[listnum][listnum2] = calculateList[listnum][listnum2] + symbol
            calculateList,listnum,listnum2 = append(calculateList,listnum,listnum2)
            display = display + symbol
            displayElement.setText(display)
            prevSymbol = symbol
#Special Characters
        elif symbol == '√' or symbol == 'x^2' or symbol == '1/x'\
             or symbol == '+ / -' or symbol == '%' or symbol == 'sin'\
             or symbol == 'cos' or symbol == 'tan' or symbol == 'sin-1'\
             or symbol == 'cos-1' or symbol == 'tan-1' or symbol == 'log'\
             or symbol == 'ln' or symbol == '10^x':
            try:
                if display == '':
                    calculateList = [[prevResult]]
                    calculateList[listnum][listnum2] = special(calculateList[listnum][listnum2],symbol)
                if prevSymbol == ')' and symbol != '+ / -':
                    calculateList[listnum - 1] = [special(eval(''.join(calculateList[listnum - 1])),symbol)]
                    display2,display = calculateList[listnum - 1], display + symbol
                    displayElement.setText(display)
                else:
                    calculateList[listnum][listnum2] = special(calculateList[listnum][listnum2],symbol)
                    display2,display = calculateList[listnum][listnum2],display + symbol
            except: continue
#Memory
        elif symbol == 'MC' or symbol == 'M+' or symbol == 'M-' \
             or symbol == 'MR' or symbol == 'MS':
            if symbol == 'MC':
                mem = '0'
            elif symbol == 'MR':
                calculateList[listnum][listnum2] = mem
            elif symbol == 'MS':
                mem = display2
            else:
                try:
                    mem = memory(symbol,display2,mem)
                except: continue
            memoryElement.undraw()
            if symbol != 'MC':
                memoryElement = Text(Point(memP.getX()+(len(mem)*.23),
                                           memP.getY()),'Memory: ' + mem)
                memoryElement.draw(win)
            if symbol == 'MS':
                continue
            displayElement.setText(display)
#Scientific Mode
        elif symbol == 'Scientific \n Mode':
            sci = sciMode(sci)
            continue
#Numbers
        else:
            calculateList[listnum][listnum2] = calculateList[listnum][listnum2] + symbol
            display = display + symbol
            display2 = calculateList[listnum][listnum2]
            prevSymbol = symbol
        print(calculateList,'\nDisplay: ', display, '\nDisplay2: ', display2,'\nListnum and L2', listnum,listnum2,'\n')
        displayElementAns.setText(display2)

main()
