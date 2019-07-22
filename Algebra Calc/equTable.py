import pandas as pd
from sympy import *


def table():
    x1 = Symbol('x1')
    y = []
    z = int(input("How many items are there?: "))
    v =  input("What is the equ?: ")
    x1 = 0
    f = Function('f')(x1)
    for x1 in range(z):
        f = Function('f')(x1)
        f = "{}".format(v)
        fx = f.replace('x', '{}'.format(x1))
        fx1 = eval(fx)
        x1 = x1 + 1
        y.append(fx1)
    y1 = "f(x) = {}".format(f)
    d = {y1 : y}
    df = pd.DataFrame(d)
    print(df)

table()
