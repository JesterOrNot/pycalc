#! /usr/bin/python3.7
def les():
    def slope():
        y1 = float(input('What is y1?: '))
        y2 = float(input('What is y2?: '))
        x1 = float(input('What is x1?: '))
        x2 = float(input('What is x2?: '))
        slope = (y2 - y1)/(x2 - x1)
        b = ((slope * x1)*-1) + y1
        print('y = {}x + {}'.format(slope, b))
    slope()
les()
#The method I used for finding the equ for b was via reorganizing
# y = mx + b
# -b     -b
# y - b = mx
# -y      -y
# -b = mx - y
# (-b)*-1 = (mx -y)*-1
# b = -mx + y