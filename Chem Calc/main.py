#! /usr/bin/python3.7
print(
    'Welcome! This is the Chem calc available calculators are Combined Gas Law(cgl), Ideal gas law(igl), Heat Equasion(he), Enthalpy Equasion(ee)'
)
while True:
    def calc():
        userInt = input('What calculator do you want?: ').lower()
        if userInt == 'he':
            import he
        elif userInt == 'cgl':
            import cglv2
        elif userInt == 'igl':
            import igl
        elif userInt == 'ee':
            import ee
        elif userInt == 'exit':
            exit()
        else:
            print('Calculator not found sorry :(')
        calc()
    calc()
# this reads usr input so that the user can navigate the chem calc