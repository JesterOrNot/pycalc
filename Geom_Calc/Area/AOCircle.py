#! /usr/bin/python3.7
from math import pi
def aoc():
	r = float(input("What is the radius?: "))
	a = pi * (r ** 2)
	print("A = {}".format(a))
aoc()