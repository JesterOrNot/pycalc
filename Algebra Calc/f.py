import sympy
def factor():
    equ = input("What is the Equasion that we are factoring?: ")
    b = sympy.factor(equ)
    print(b)
while True:
    try:
        factor()
        break
    except ValueError:
        print("Something Went Wrong: Tip 2x = 2*x")