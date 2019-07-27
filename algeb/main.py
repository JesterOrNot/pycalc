#! /usr/bin/python3.7
import os
print('Welcome! Tins is a algebra calculator, available calculators include: Linear Equation from 2 points(les), quadratic equation (quad), absolute value(av), Factor equations(factor), Zero product property(zpp), Greatest common factor calculator(gcf), Line of symmetry calc(los), standard form quadratics grapher(sfqg), graphing calc(graphcalc), evaluate exponential functions(eef), function table(ft)')
while True:
    def calc():
        userInt = input('What calculator do you want?: ').lower()
        if userInt in 'les':
            import algeb.linEquSolv
        elif userInt in 'quad, quadratic':
            import algeb.quad
        elif userInt in 'av':
            import algeb.AbsVal
        elif userInt in 'factor':
            import algeb.factor
        elif userInt in 'zpp':
            import algeb.zeroProdProp
        elif userInt in 'gcf':
            import algeb.GCF
        elif userInt in 'los':
            import algeb.linOfSym
        elif userInt in 'sfqg':
            import algeb.standFormQuadFunc
        elif userInt in 'eef':
            import algeb.evalExpFun
        elif userInt in 'ft':
            import algeb.funcTable
        elif userInt in 'graphcalc':
            os.chdir('graph')
            os.system('python3 ./main.py')
        elif userInt == 'exit':
            exit()
        else:
            print('Error something went wrong. Please try again')
    calc()


# This is the  controller file for the algebra calculator this is where the user input is read and is used to access the diffrent functions of the calculator
