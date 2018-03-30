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
