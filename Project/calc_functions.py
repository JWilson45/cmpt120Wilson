import math
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def changeSign(x):
    x = float(x) * -1
    x = str(x)
    if x[-2:] == '.0':
        x = x[:-2]
    return x

def percent(x):
    x = float(x) / 100
    return str(x)

def sqr(x):
    x = float(x) ** 2
    return str(x)

def root(x):
    x = math.sqrt(float(x))
    return str(x)

def oneOverx(x):
    x = 1 / float(x)
    return str(x)

def setup(string):
    x = float(string[0])
    y = float(string[2])
    return x,y

def determine(string):
    if string[1] == '+':
        x,y = setup(string)
        string = add(x,y)
    elif string[1] == 'x':
        x,y = setup(string)
        string = multiply(x,y)
    elif string[1] == '/':
        x,y = setup(string)
        string = divide(x,y)
    elif string[1] == '-':
        x,y = setup(string)
        string = subtract(x,y)
    return string

def special(num,operator):
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
    if ans[-2:] == '.0':
        ans = ans[:-2]
    return ans
    
def memory(symbol,num,mem):
    if symbol == 'M+':
        mem = str(add(float(mem),float(num)))
    elif symbol == 'M-':
        mem = str(subtract(float(mem),float(num)))
    if mem[-2:] == '.0':
        mem = mem[:-2]
    return str(mem)
    
