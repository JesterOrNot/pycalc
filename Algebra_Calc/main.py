#! /usr/bin/python3.7
import os
print('Welcome! Tnis is a algebra calculator, available calculators include: Linear Equasion from 2 points(les), quadratic equasion (quad), absolute value(av), Factor equasions(factor), Zero product propertey(zpp), Greatest common factor calculator(gcf), Line of symmetrey calc(los), standard form quadratics grapher(sfqg), graphing calc(graphcalc), evaluate exponential functions(eef), function table(ft)')
while True:
    def calc():
        userInt = input('What calculator do you want?: ').lower()
        if userInt in 'les':
            import algebra_calc.linEquSolv
        elif userInt in 'quad, quadratic':
            import algebra_calc.quad
        elif userInt in 'av':
            import algebra_calc.AbsVal
        elif userInt in 'factor':
            import algebra_calc.factor
        elif userInt in 'zpp':
            import algebra_calc.zeroProdProp
        elif userInt in 'gcf':
            import algebra_calc.GCF
        elif userInt in 'los':
            import algebra_calc.linOfSym
        elif userInt in 'sfqg':
            import algebra_calc.standFormQuadFunc
        elif userInt in 'eef':
            import algebra_calc.evalExpFun
        elif userInt in 'ft':
            import algebra_calc.funcTable
        elif userInt in 'graphcalc':
            os.chdir('graph')
            os.system('python3 ./main.py')
        elif userInt == 'exit':
            exit()
        else:
            print('Error something went wrong. Please try again')
    calc()


# This is the  controller file for the algebra calculator this is where the user input is read and is used to access the diffrent functions of the calculator
