import sympy
def simp():
    userInt = input("What equation are we solving with the ZPP?: ")
    x = sympy.solve(userInt)
    print('The Awnser is: {}'.format(x))
simp()