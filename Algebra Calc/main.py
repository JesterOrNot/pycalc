#! /usr/bin/python3.7
import os
print('Welcome! Tnis is a algebra calculator, available calculators include: Linear Equasion from 2 points(les), quadratic equasion (quad), absolute value(av), Factor equasions(factor), Zero product propertey(zpp), Greatest common factor calculator(gcf), Line of symmetrey calc(los), standard form quadratics grapher(sfqg), graphing calc(graphcalc)')
while True:
    def calc():
        userInt = input('What calculator do you want?: ').lower()
        if userInt in 'les':
            import les
        elif userInt in 'quad, quadratic':
            import quad
        elif userInt in 'av':
            import av
        elif userInt in 'factor':
            import f
        elif userInt in 'zpp':
            import zpp
        elif userInt in 'gcf':
            import gcf
        elif userInt in 'los':
            import los
        elif userInt in 'sfqg':
            import sfqg
        elif userInt in 'graphcalc':
            os.chdir('graph')
            os.system('python3 ./main.py')
        elif userInt == 'exit':
            exit()
        else:
            print('Error something went wrong. Please try again')
    calc()


# This is the  controller file for the algebra calculator this is where the user input is read and is used to access the diffrent functions of the calculator
