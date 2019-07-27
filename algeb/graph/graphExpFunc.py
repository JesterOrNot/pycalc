import numpy as np
import numpy
import matplotlib.axis
import matplotlib.pyplot as plt
import sympy
import math
dict1 = {
}

def exponentialbaseb():
    a = float(input("What is a?: "))
    dict1.update({"a": a})
    b = float(input("What is b?: "))
    dict1.update({"b": b})
    formula = '{} * {}**x'.format(a, b)

    def graph(formula):
        x = np.linspace(-10, 10)
        y = eval(formula)
        plt.plot(x, y, color='k')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(axis='both', which='both')
        plt.show()
    graph(formula)


def exponential_growth():
    a = float(input("What is a?: "))
    dict1.update({"a": a})
    r = float(input("What is r?: "))
    dict1.update({"r": r})
    formula = '{}*(1 + {})**x'.format(a, r)

    def graph(formula):
        x = np.linspace(-10, 10)
        y = eval(formula)
        plt.plot(x, y, color='k')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(axis='both', which='both')
        plt.show()
    graph(formula)


def exponential_decay():
    a = float(input("What is a?: "))
    dict1.update({"a": a})
    r = float(input("What is b?: "))
    dict1.update({"r": r})
    formula = '{}*(1 - {})**x'.format(a, r)

    def graph(formula):
        x = np.linspace(-10, 10)
        y = eval(formula)
        plt.plot(x, y, color='k')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(axis='both', which='both')
        plt.show()
    graph(formula)


def choose():
    print("Welcome to the exponential equasion grapher! Current options include: exponential growth grapher, exponential decay grapher or baseb?")
    userInt = input("What do you want?: ")
    if userInt in 'ef':
        exponentialbaseb()
    elif userInt in 'eg':
        exponential_growth()
    elif userInt in 'ed':
        exponential_decay()


choose()