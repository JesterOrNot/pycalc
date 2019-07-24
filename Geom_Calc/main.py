#! /usr/bin/python3.7


import os
print("Welcome to the geometry calculator avaliable calculators include: area finder (af), pythagTheo(pt), sin cos tan finder(sct), trigonometric table(tt)")
while True:
	def chooseCalc():
		userInt = input("What do you want to use?: ").lower()
		if userInt == "af":
			os.chdir('Area')
			os.system('python3 ./main.py')
		elif userInt == 'pt':
			import geom_calc.pythagTheo
		elif userInt == 'sct':
			import geom_calc.SinCosTan
		elif userInt == 'tt':
			import geom_calc.sincostan
		elif userInt == 'exit':
			exit()
	chooseCalc()
chooseCalc()