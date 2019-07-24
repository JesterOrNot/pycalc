#! /usr/bin/python3.7
print(
    'Welcome! This is the Chem calc available calculators are Combined Gas Law(cgl), Ideal gas law(igl), Heat Equasion(he), Enthalpy Equasion(ee)'
)
while True:
    def calc():
        userInt = input('What calculator do you want?: ').lower()
        if userInt == 'he':
            import chem_calc.heatEqu
        elif userInt == 'cgl':
            import chem_calc.combGasLaw
        elif userInt == 'igl':
            import chem_calc.IdeGasLaw
        elif userInt == 'ee':
            import chem_calc.enthEqu
        elif userInt == 'exit':
            exit()
        else:
            print('Calculator not found sorry :(')
        calc()
    calc()
# this reads usr input so that the user can navigate the chem calc