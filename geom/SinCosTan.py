#! /usr/bin/python3.7


# soh cah toa
def sin():
	o = float(input('What is the oppisite?: '))
	h = float(input("What is the hypotnuse?: "))
	s = o / h
	print("sin = {}".format(s))
def cos():
	a = float(input('What is the ajacent?: '))
	h = float(input("What is the hypotnuse?: "))
	c = a / h
	print('cos = {}'.format(c))
def tan():
	o = float(input("What is the oppisite?: "))
	a = float(input("What is the ajacent?: "))
	t = o / a
	print("tan = {}".format(t))
def main():
	userInt = input('What are we solving for (sin cos or tan)?: ').lower()
	if userInt == 'sin':
		sin()
	elif userInt == 'cos':
		cos()
	elif userInt == 'tan':
		tan()
	else:
		print('An error has occured please try again')
main()