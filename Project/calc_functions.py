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
    return str(x)

def percent(x):
    x = float(x) / 100
    return str(x)

def setup(string):
    x = float(string[0])
    y = float(string[2])
    return x,y
    
def determine(string):
    if string[1] == '+':
        x,y = setup(string)
        string = str(add(x,y))
    elif string[1] == 'x':
        x,y = setup(string)
        string = str(multiply(x,y))
    elif string[1] == '/':
        x,y = setup(string)
        string = str(divide(x,y))
    elif string[1] == '-':
        x,y = setup(string)
        string = str(subtract(x,y))
    else: return 'Error'
    return string
