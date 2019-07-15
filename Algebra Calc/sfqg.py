from math import sqrt
import sympy
dict1 ={
	
}
def get_Value():
	a = float(input("What is a?: "))
	dict1.update({"a":a})
	b = float(input("What is b?: "))
	dict1.update({"b":b})
	c = float(input("What is c?: "))
	dict1.update({"c":c})
def lineOfSym():
	a = dict1.get("a")
	b = dict1.get("b")
	los = b*-1/2*a
	dict1.update({"los":los})
	print('The line of symemetey is x = {}'.format(los))
def quad():
	a = dict1.get("a")
	b = dict1.get("b")
	c = dict1.get("c")
	xplus = ( (b * -1) + (sqrt( (b ** 2) - (4* a * c) )) ) / (2 * a)
	xminus = ( (b * -1) - (sqrt( (b ** 2) - (4* a * c) )) ) / (2 * a)
	print('The x intercepts are {} and {}'.format(xplus, xminus))
def vertex():
    a = dict1.get("a")
    b = dict1.get("b")
    c = dict1.get("c")
    los = dict1.get("los")
    a1 = a*los**2
    b1 = b*los
    c1 = c
    y = a1 + b1 + c1
    print("The vetex is ({},{})".format(los, y))
get_Value()
lineOfSym()
vertex()
try:
	quad()
except ValueError:
    print("There is not x intercept")