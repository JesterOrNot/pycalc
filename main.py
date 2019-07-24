#! /usr/bin/python3.7


import os
print("This is the main menu of the calculator The options are the Chem calc(cc), the algebra calc (ac), the geom calc (gc) or the physics calculator (pc), and misc calc (mc)")
z = 0
while z == 0:
	def chooseCalc():
		userInt = input('What Calc do you want?: ').lower()
		if userInt == 'cc':
			os.chdir('Chem Calc')
			os.system('python3 ./main.py')
		elif userInt == 'ac':
			os.chdir('Algebra Calc')
			os.system('python3 ./main.py')
		elif userInt == 'gc':
			os.chdir('Geom Calc')
			os.system('python3 ./main.py')
		elif userInt == 'pc':
			os.chdir('Physics Calc')
			os.system('python3 ./main.py')
		elif userInt == 'mc':
			os.chdir("Misc_Calculators")
			os.system("python3 ./main.py")
		elif userInt == 'exit':
			exit()
		else:
			print('An error has occured :( please try again')
	chooseCalc()

# This is the main controller file where the main meunu when you start the application is controlled this script uses the os module to change the directory so that it can run the disired program's controller (main.py)