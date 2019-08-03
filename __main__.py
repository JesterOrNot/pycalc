#! /usr/bin/python3.7


import os

print("This is the main menu of the calculator \n The options are the Chem calc(cc), the algebra calc (ac), the geom calc (gc) or the physics calculator (pc), and misc calc (mc)")
z = 0
while z == 0:
    def chooseCalc():
        userInt = input('What Calc do you want?: ').lower()
        if userInt == 'cc':
            os.chdir('chem')
            os.system('python3 ./main.py')
        elif userInt == 'ac':
            os.chdir('algeb')
            os.system('python3 ./main.py')
        elif userInt == 'gc':
            os.chdir('geom')
            os.system('python3 ./main.py')
        elif userInt == 'pc':
            os.chdir('phys')
            os.system('python3 ./main.py')
        elif userInt == 'mc':
            os.chdir("misc")
            os.system("python3 ./main.py")
        elif userInt == 'exit':
            exit()
        else:
            print('An error has ocurred :( please try again')
    chooseCalc()
    if __name__ == "__main__":
        chooseCalc()
# This is the main controller file where the main menu when you start the application is controlled this script uses the os module to change the directory so that it can run the disired program's controller (main.py)
