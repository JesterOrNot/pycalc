#! /usr/bin/python3.7
# This is a lorentz factor calc
import math

def lf():
    v = float(input('What is v?: '))
    c = float(input("What is c?: "))
    equ = 1 / math.sqrt(1-((v ** 2)/(c**2)))
    print(equ)
lf()
