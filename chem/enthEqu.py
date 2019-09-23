#! /usr/bin/python3
elements = {
  "O2(g)": 0,
  "C2H2(g)": 226.7,
  "C2H4(g)": 52.3,
  "C2H6(g)": -84.7,
  "C3H8(g)": -103.8,
  "C4H10(g)": -124.7,
  "C5H12(l)": -173.1,
  "C2H5OH(l)": -277.6,
  "CoO(s)": -239.3,
  "Cr2O3(s)": -1128.4,
  "CuO(s)": -155.2,
  "Cu2O(s)": -166.7,
  "CuS(s)": -48.5,
  "CuSO4(s)": -769.9,
  "Fe2O3(s)": -822.2,
  "Fe3O4(s)": -1120.9,
  "HBr(g)": -36.2,
  "HCl(g)": -92.3,
  "HF(g)": -268.6,
  "HI(g)": 25.9,
  "HNO3(l)": -173.2,
  "H2O(g)": -241.8,
  "NH4Cl(s)": -315.4,
  "NH4NO3(s)": -365.1,
  "NO(g)": 90.25,
  "NO2(g)": 33.18,
  "NiO(s)": -244.3,
  "PbBr2(s)": -277,
  "PbCl2(s)": -359.2,
  "PbO(s)": -217.9,
  "PbO2(s)": -276.6,
  "Pb3O4(s)": -734.7,
  "PCl3(g)": -306.4,
  "PCl5(g)": -398.9,
  "SiO2(s)": -859.4,
  "AgBr(s)": -99.5,
  "AgCl(s)": -127.0,
  "AgI(s)": -62.4,
  "Ag2O(s)": -30.6,
  "Ag2S(s)": -31.8,
  "Al2O3(s)": -1669.8,
  "BaCl2(s)": -860.1,
  "BaCO3(s)": -1218.8,
  "BaO(s)": -558.1,
  "BaSO4(s)": -1465.2,
  "CaCl2(s)": -795.0,
  "CaCO3": -1207.0,
  "CaO(s)": -635.5,
  "Ca(OH)2(s)": -986.6,
  "CaSO4(s)": -1432.7,
  "CCl4(l)": -139.5,
  "CH4(g)": -74.8,
  "CHCl3(l)": -131.8,
  "CH3OH(l)": -238.6,
  "CO(g)": -110.5,
  "CO2(g)": -393.5,
  "H2O(l)": -285.8,
  "H2(g)": 0,
  "SO2(g)": -296.8,
  "SO3(g)": -395.7,
  "N2O4(g)": 9.16,
  "B5H9(g)": 73.2,
  "B2O3(g)": -1272.77,
}


def EE():
    c = 0
    while c == 0:
        x = int(input('How many reactants are there?: '))
        y = int(input('How many products are there?: '))
        r = []
        s = []
        while len(r) != x:
            m = input('What are the reactants?: ')
            if m in elements:
                r.append(elements[m])
            else:
                print('Sorry this is not in the database yet :(')
        sum_of_r = sum(r)
        while len(s) != y:
            n = input('What are the products?: ')
            if n in elements:
                s.append(elements[n])
            else:
                print('Sorry this is not in the database yet :(')
            sum_of_p = sum(s)
            e = (sum_of_p - sum_of_r)
            print(f'ΔH = {e} KJ')
            break


EE()
