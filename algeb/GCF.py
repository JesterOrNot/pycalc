#! /usr/bin/python3.7
import sympy
def test2():
    usrInt = input('What numbers are we getting the gcf of?: ')
    my_list = usrInt.replace(" "," ").split(",")
    z = sympy.gcd_list(my_list)
    print(z)
test2()