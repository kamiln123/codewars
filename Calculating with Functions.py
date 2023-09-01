#kalkulator stworzony za pomocą funkcji
#np. four(plus(nine())) =13
def zero(arg=None):# każda funkcja zawierająca liczbę może być albo samą liczbą albo funkcją
    if arg:
        return arg(0)
    else:
        return 0
def one(arg=None):
    if arg:
        return arg(1)
    else:
        return 1
def two(arg=None):
    if arg:
        return arg(2)
    else:
        return 2
def three(arg=None):
    if arg:
        return arg(3)
    else:
        return 3
def four(arg=None):
    if arg:
        return arg(4)
    else:
        return 4
def five(arg=None):
    if arg:
        return arg(5)
    else:
        return 5
def six(arg=None):
    if arg:
        return arg(6)
    else:
        return 6
def seven(arg=None):
    if arg:
        return arg(7)
    else:
        return 7
def eight(arg=None):
    if arg:
        return arg(8)
    else:
        return 8
def nine(arg=None):
    if arg:
        return arg(9)
    else:
        return 9

def plus(x):
    return lambda y: y+x
def minus(x):
    return lambda y: y-x
def times(x):
    return lambda y: y*x
def divided_by(x):
    return lambda y: int(y/x) 
