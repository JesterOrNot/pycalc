#! /usr/bin/python3.7
import math
from sympy import *
dict1 = {
    
}
def gcf():
    num1 = int(input('What is the first number?: '))
    num2 = int(input('What is the second number?: '))
    gcf = math.gcd(num1, num2)
    dict1.update({"gcf":gcf})
    print('The GCF of {} and {} is {}.'.format(num1, num2, gcf))
while True:
    try:
        gcf()
        break
    except ValueError:
        print("You can't use a decimal, please try again")
        gcf()