#! /usr/bin/python3.7
import os
print("Welcome to the physics calculator available calculators include: distance speed time calculator (dstc), gravity formula(gf), lorentz factor(lf), mass energy(mee),line displacement(ld), velocity (velocity) acceleration(acceleration), range(range)")
while True:
    keywords1 = ["dst", "dtc"]
    keywords2 = ['grav', 'gf']

    def chooseCalc():
        userInt = input("Which calculator do you want?: ").lower()
        if userInt in keywords1:
            import phys.distspeed
        elif userInt in keywords2:
            import phys.gravforce
        elif userInt == 'lf':
            import phys.lorenfact
        elif userInt == 'me':
            import phys.massEner
        elif userInt == 'ld':
            import phys.lineDisplace
        elif userInt in "velocity":
            import phys.velocity
        elif userInt in "acceleration":
            import phys.accelerate
        elif userInt in "range":
            import phys.range
        elif userInt == 'exit':
            exit()
        else:
            print("An error has occurred")
    chooseCalc()
chooseCalc()
