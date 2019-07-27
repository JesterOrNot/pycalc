#! /usr/bin/python3.7
print(
    'Welcome! This is the Chem calc available calculators are Combined Gas Law(cgl), Ideal gas law(igl), Heat Equation(he), Enthalpy Equation(ee)'
)
while True:
    def calc():
        userInt = input('What calculator do you want?: ').lower()
        if userInt == 'he':
            import chem.heatEqu
        elif userInt == 'cgl':
            import chem.combGasLaw
        elif userInt == 'igl':
            import chem.IdeGasLaw
        elif userInt == 'ee':
            import chem.enthEqu
        elif userInt == 'exit':
            exit()
        else:
            print('Calculator not found sorry :(')
        calc()
    calc()
# this reads usr input so that the user can navigate the chem calc
