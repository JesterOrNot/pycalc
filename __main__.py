#! /usr/bin/env python3


import os

print(
    "This is the main menu of the calculator \n The options are the Chem calc(cc), the algebra calc (ac), the geom calc (gc) or the physics calculator (pc), and misc calc (mc)"
)
Z = 0
while Z == 0:
    def main():
        userint = input('What Calc do you want?: ').lower()
        if userint == 'cc':
            os.chdir('chem')
            os.system('python3 ./main.py')
        elif userint == 'ac':
            os.chdir('algeb')
            os.system('python3 ./main.py')
        elif userint == 'gc':
            os.chdir('geom')
            os.system('python3 ./main.py')
        elif userint == 'pc':
            os.chdir('phys')
            os.system('python3 ./main.py')
        elif userint == 'mc':
            os.chdir("misc")
            os.system("python3 ./main.py")
        elif userint == 'exit':
            exit()
        else:
            print('An error has ocurred :( please try again')
<<<<<<< HEAD:__main__.py
    chooseCalc()
    if __name__ == "__main__":
        chooseCalc()
=======
    main()
>>>>>>> 3e0a41779841728b80f24823d4ba131955c01cab:main.py
# This is the main controller file where the main menu when you start the application is controlled this script uses the os module to change the directory so that it can run the disired program's controller (main.py)
