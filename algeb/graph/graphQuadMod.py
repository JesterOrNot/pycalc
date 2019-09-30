import numpy as np
import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.axis
from sympy import *


def standard():
    a = input("What is a?: ")
    b = input("What is b?: ")
    c = input("What is c?: ")
    formula = '{}*x**2 + {}*x + {}'.format(a, b, c)

    def graph(formula):
        x = np.linspace(-10, 10)
        y = eval(formula)
        plt.plot(x, y)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.xlim((-10, 10))
        plt.ylim((-10, 10))
        plt.grid(axis='both', which='both')
        plt.show()
    graph(formula)


def vertex():
    a = input("What is a?: ")
    h = input("What is h?: ")
    k = input("What is k?: ")
    formula = '{}*(x - {})**2 + {}'.format(a, h, k)
    def graph(formula):
        x = np.linspace(-10, 10)
        y = eval(formula)
        plt.plot(x, y)
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.xlim((-5, 5))
        plt.ylim((-5, 5))
        plt.grid(axis='both', which='both')
        plt.show()
    graph(formula)


def menu():
    print("What is the equasion type vertex form or standard form")
    userInt = input("Which one do you want?: ").lower()
    if userInt in 'vertex':
    	vertex()
    elif userInt in 'standard':
    	standard()
    else:
        print("That is not an option.")
menu()