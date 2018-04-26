from graphics import *
from button import Button

win = GraphWin("Calculator",450,425)
win.setCoords(0,0,9,8)
buttonSpecs = [(1,1,'('),(2,1,')'),(3,1,'MS'),(4,1,'Sci \n Mode'),(5,1,'0'),(6,1,'.'),(7,1,'='),(8,1,'10^x'),
               (1,2,'log'),(2,2,'ln'),(3,2,'MR'),(4,2,'1'),(5,2,'2'),(6,2,'3'),(7,2,'+'),(8,2,'x^y'),
               (1,3,'tan'),(2,3,'tan-1'),(3,3,'M-'),(4,3,'4'),(5,3,'5'),(6,3,'6'),(7,3,'-'),(8,3,'1/x'),
               (1,4,'cos'),(2,4,'cos-1'),(3,4,'M+'),(4,4,'7'),(5,4,'8'),(6,4,'9'),(7,4,'x'),(8,4,'x^2'),
               (1,5,'sin'),(2,5,'sin-1'),(3,5,'MC'),(4,5,'Clear'),(5,5,'+ / -'),(6,5,'%'),(7,5,'/'),(8,5,'√')]

buttons = []
for cx, cy, label in buttonSpecs:
    buttons.append(Button(win, Point(cx, cy), .75, .75, label))
for b in buttons:
    b.activate()

scientificButts = (buttons[7],buttons[8],buttons[9],buttons[15],buttons[16],buttons[17],buttons[24],buttons[25],buttons[32],buttons[33])
for b in scientificButts:
    b.deactivate()

acc,memP = Rectangle(Point(.6, 6),Point(8.4, 7.5)),Point(3.5, 25)
acc.setFill('LightGreen')
acc.draw(win)
displaySci = Text(Point(memP.getX()+.5,memP.getY() -2.5),'Scientific Mode')

def getclick():
    while True:
        click = win.getMouse()
        for b in buttons:
            if b.clicked(click):
                return b.getLabel()

def sciMode(sci):
    if sci:
        sci = False
        for b in scientificButts:
            b.deactivate()
    elif not sci:
        sci = True
        for b in scientificButts:
            b.activate()
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
        symbol = getclick()
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
        elif symbol == 'Sci \n Mode':
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
