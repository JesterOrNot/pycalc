#! /usr/bin/python3.7
def lineOfSym():
    print('Welcome this is the line of symetrey calc')
    b = float(input('What is b?: '))
    a = float(input('What is a?: '))
    los = (b*-1) / (2*a)
    print('The line of symemetey is x = {}'.format(los))


lineOfSym()
