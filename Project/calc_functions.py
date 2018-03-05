def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def changeSign(x):
    x = x[:-1]
    x = x + '* -1'
    x = eval(x)
    x = str(x)
    return x

def percent(x):
    x = x[:-1]
    x = x + '/ 100'
    x = eval(x)
    x = str(x)
    return x

def setup(string):
    x = float(string[0])
    y = float(string[1])
    return x,y
    
def determine(string):
    string = string[:-1]
    if '+' in string:
        string = string.split('+')
        x,y = setup(string)
        string = add(x,y)
        string = str(string)
        return string
    if 'x' in string:
        string = string.split('x')
        x,y = setup(string)
        string = multiply(x,y)
        string = str(string)
        return string
    if '/' in string:
        string = string.split('/')
        x,y = setup(string)
        string = divide(x,y)
        string = str(string)
        return string
    if '-' in string:
        if string.count('-') > 1:
            return 'Cant subrtact negitives yet'
        string = string.split('-')
        x,y = setup(string)
        string = subtract(x,y)
        string = str(string)
        return string

    else: return 'Error'
