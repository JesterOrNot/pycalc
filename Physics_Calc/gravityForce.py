#! /usr/bin/python3.7


from scipy.constants import G
def fogc():
	M = float(input('What is the weight of the first mass in kg?: '))
	m = float(input('What is the weight of the second mass in kg?: '))
	R = float(input("What is  the distance between the two masses in meters?: "))
	F = (G * M * m) / (R**2)
	print("The gravitational force is {} N".format(F))
	fogc()
fogc()