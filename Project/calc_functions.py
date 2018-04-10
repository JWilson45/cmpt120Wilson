import math
def rm0(x):
    x = str(x)
    if x[-2:] == '.0':
        x = x[:-2]
        return x
    else: return x

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def changeSign(x):
    x = x * -1
    return x

def sin(x):
    x = math.sin(x)
    return x

def cos(x):
    x = math.cos(x)
    return x

def tan(x):
    x = math.tan(x)
    return x

def sin1(x):
    x = math.sinh(x)
    return x

def cos1(x):
    x = math.cosh(x)
    return x

def tan1(x):
    x = math.tanh(x)
    return x

def logerithm(x):
    x = math.log10(x)
    return x

def ln(x):
    x = math.log(x)
    return x

def tenx(x):
    x = 10 ** x
    return x

def percent(x):
    x = x / 100
    return x

def sqr(x):
    x = x ** 2
    return x

def root(x):
    x = str(x)
    if x[0] == '-':
        return 'Error'
    x = float(x)
    x = math.sqrt(x)
    return x

def oneOverx(x):
    x = 1 / x
    return x

def displaySet(calculateList):
    dis = ''
    dis = dis.join(calculateList)
    print(dis)
    return dis 

def evaluate(lis):
    string = eval(''.join(lis))
    string = rm0(string)
    return string

def special(num,operator):
    num = float(num)
    if operator == '√':
        ans = root(num)
    elif operator == 'x^2':
        ans = sqr(num)
    elif operator == '1/x':
        ans = oneOverx(num)
    elif operator == '+ / -':
        ans = changeSign(num)
    elif operator == '%':
        ans = percent(num)
    elif operator == 'sin':
        ans = sin(num)
    elif operator == 'cos':
        ans = cos(num)
    elif operator == 'tan':
        ans = tan(num)
    elif operator == 'sin-1':
        ans = sin1(num)
    elif operator == 'cos-1':
        ans = cos1(num)
    elif operator == 'tan-1':
        ans = tan1(num)
    elif operator == 'log':
        ans = logerithm(num)
    elif operator == 'ln':
        ans = ln(num)
    elif operator == '10^x':
        ans = tenx(num)
    ans = rm0(ans)
    return ans
    
def memory(symbol,num,mem):
    num, mem = float(num),float(mem)
    if symbol == 'M+':
        mem = add(mem,num)
    elif symbol == 'M-':
        mem = subtract(mem,num)
    mem = rm0(mem)
    return mem

def reset():
    dis,lst,lstnum,dis2 = '',[''],0,''
    return dis,lst,lstnum,dis2

def append(calculateList,listnum):
    calculateList.append('')
    listnum = listnum + 1
    return calculateList,listnum

def operatortest(symbol,display2,calculateList,display):
    if symbol == 'x':
        symbol = '*'
    if symbol == 'x^y':
        symbol = '**'
    if display == '':
        calculateList = [display2]
    return calculateList, symbol
    
##def parenthesisTest(clist,sym):
##    parent,parentOpen,parentClose = -1,-1,-1
##    if sym == ')':
##        for i in clist:
##            parent += 1
##            if i == '(':
##                parentOpen += 1
##            elif i == ')':
##                parentClose += 1
##    return parentOpen, parentClose
