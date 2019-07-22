from sympy import collect
from sympy.abc import *


def evalExpFunc():
    varVal = float(input("What is the value of the exponent's variable?: "))
    a = input('what is starting value?: ')
    a1 = eval(a)
    b = input("What is b?: ")
    b1 = eval(b)
    equ = '{}*({})**{}'.format(a1, b1, varVal)
    awnser = eval(equ)
    print('The awnser is: {}'.format(awnser))


def evalExpProp():
    expr = input('What exponential equ are we simplifying?: ')
    collected_expr = collect(expr, x)
    print(collected_expr)
def choose():
    print('The options are: simplifying exponentials(se) and evaluating exponential equasions(eee)')
    userInt = input('What do you want?: ')
    if userInt in 'se':
        evalExpProp()
    elif userInt in 'eee':
        evalExpFunc()
    else:
        print("error please try again")
        choose()


choose()