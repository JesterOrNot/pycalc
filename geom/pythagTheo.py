#! /usr/bin/python3.7
def pyth():
	a = float(input("What is a?: "))
	b = float(input("What is b?: "))
	h = (a ** 2) + (b ** 2)
	print("The hypot of the triangle is {}".format(h))
pyth()