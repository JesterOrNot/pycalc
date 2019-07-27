#! /usr/bin/python3.7


print("Welcome to the physics calculator available calculators include: distance speed time calculator (dstc), gravity formula(gf), lorentz factor(lf)")
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
        elif userInt == 'exit':
            exit()
        else:
            print("An error has occured")
    chooseCalc()
chooseCalc()
