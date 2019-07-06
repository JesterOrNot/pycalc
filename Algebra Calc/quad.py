#! /usr/bin/python3.7


from math import sqrt
a = float(input('What is a?: '))
b = float(input('What is b?: '))
c = float(input('What is c?: '))
xplus = ( (b * -1) + (sqrt( (b ** 2) - (4* a * c) )) ) / (2 * a)
xminus = ( (b * -1) - (sqrt( (b ** 2) - (4* a * c) )) ) / (2 * a)
print('x = {} or x = {}'.format(xplus, xminus))