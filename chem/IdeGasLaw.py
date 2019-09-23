#!/usr/bin/python3


def igl():
    unknown = input("What is the unknown variable? (P,V,n,T): ").lower()
    R = 0.0821
    if unknown in 'p':
        V = float(input("What is the volume (in liters) of the gas?: "))
        n = float(input("How many moles of the gas are present?: "))
        T = float(input("What is the temperature of the gas (in K?): "))
        P = (n*R*T)/V
        print(f"P = {P} atm.")
    if unknown in 'v':
        P = float(input("What is the pressure (in atm) of the gas?: "))
        n = float(input("How many moles of the gas are present?: "))
        T = float(input("What is the temperature of the gas (in K?): "))
        V = (n*R*T)/P
        print(f"V = {V} liters.")
    if unknown in 'n':
        P = float(input("What is the pressure (in atm) of the gas?: "))
        V = float(input("What is the volume (in liters) of the gas?: "))
        T = float(input("What is the temperature of the gas (in K?): "))
        n = (P*V)/(R*T)
        print(f"n = {n} moles.")
    if unknown in 't':
        P = float(input("What is the pressure (in atm) of the gas?: "))
        V = float(input("What is the volume (in liters) of the gas?: "))
        n = float(input("How many moles of the gas are present?: "))
        T = (P*V)/(R*n)
        print(f"T = {T} degrees K.")


def convert():
    convert_or_no = input('Do we need to convert?: ').lower()
    if convert_or_no in "yes,ye,y":
        uc()
        convert()
    elif convert_or_no in 'no,n':
        igl()


def uc():
    unknown = input('What Are we converting to Temperature or pressure: ').lower()
    if unknown in 't,te,tem,temp':
        def TC():
            c = 0
            decimal = c
            f = 0
            decimal2 = f
            k = 0
            decimal3 = k
            unknown1 = input(
                'What is the starting temp in, C, K or F: ').lower()
            unknown2 = input(
                'What are we converting to, C, K or F: ').lower()
            if unknown1 == 'c' and \
               unknown2 == 'f':
                if decimal2 is str:
                    c = int(
                        input('What is the starting temp in c that you are converting?: '))
                    f = c * 1.8000 + 32
                    print(f'{f} °F')
                else:
                    c = float(
                        input('What is the starting temp in c that you are converting?: '))
                    f = c * 1.8000 + 32
                    print(f'{f} °F')
            if unknown1 in 'C, c' and \
               unknown2 in 'K, k':
                if decimal3 is str:
                    c = int(
                        input('What is the starting temp in c that you are converting?: '))
                    k = c + 273
                    print('{} °K'.format(k))
                else:
                    c = float(
                        input('What is the starting temp in c that you are converting?: '))
                    k = c + 273
                    print('{} °K'.format(k))
            if unknown1 in 'K, k' and \
               unknown2 in 'F, f':
                if decimal2 is str:
                    k = int(
                        input('What is the starting temp in k that you are converting?: '))
                    f = k * 1.8 - 459.67
                    print('{} °F'.format(f))
                else:
                    k = float(
                        input('What is the starting temp in k that you are converting?: '))
                    f = k * 1.8 - 459.67
                    print(f'{f} °F')
            if unknown1 == 'k' and unknown2 == 'c':
                if decimal is str:
                    k = int(
                        input('What is the starting temp in k that you are converting?: '))
                    c = k - 273
                    print(f'{c} °C')
                else:
                    k = float(
                        input('What is the starting temp in k that you are converting?: '))
                    c = k - 273
                    print('{} °C'.format(c))
            if unknown1 in 'F, f' and \
               unknown2 in 'K, k':
                if decimal3 is str:
                    f = int(
                        input('What is the starting temp in k that you are converting?: '))
                    k = ((f - 32)/1.8)+273/15
                    print('{} °K'.format(k))
                else:
                    f = float(
                        input('What is the starting temp in k that you are converting?: '))
                    k = ((f - 32)/1.8)+273/15
                    print('{} °K'.format(k))
            if unknown1 in 'F, f' and \
               unknown2 in 'C, c':
                if decimal is str:
                    f = int(
                        input('What is the starting temp in f that you are converting?: '))
                    c = (f - 32)/1.8
                    print(f'{c} °C')
                else:
                    f = float(
                        input('What is the starting temp in f that you are converting?: '))
                    c = (f - 32)/1.8
                    print(f'{c} °C')
        TC()
    if unknown in 'pressure, p, P':
        def PC():
            atm = 0
            decimal = atm
            torr = 0
            decimal2 = torr
            mmhg = 0
            decimal3 = mmhg
            kpa2 = 0
            decimal4 = kpa2
            unknown1 = input(
                'What are we starting with? (Kpa, Atm, Torr,Mmhg): ')
            unknown2 = input(
                'What are we converting to? (Kpa, Atm, Torr,Mmhg): ')
            if unknown1 in 'KPA, KPa, Kpa, kPA, kPa, kpA, kpa' and \
                    unknown2 in 'ATM, ATm, Atm, aTM, aTm, atM, atm':
                if decimal is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    atm = kpa / 101.325
                    print('{} atm'.format(atm))
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    atm = kpa / 101.325
                    print(f'{atm} atm')
            if unknown1 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa ' and \
                    unknown2 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR':
                if decimal2 is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    torr = kpa / 101.3
                    print(f'{torr} torr')
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    torr = kpa / 0.1333223684
                    print(f'{torr} torr')
            if unknown1 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa ' and \
                    unknown2 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG':
                if decimal3 is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    mmhg = kpa / 0.1333223684
                    print(f'{mmhg} mmhg')
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    mmhg = kpa / 0.1333223684
                    print(f'{mmhg} mmhg')
            if unknown1 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG' and \
                    unknown2 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa':
                if decimal4 is str:
                    mmhg = int(input('How much mmhg are you converting?: '))
                    kpa2 = mmhg * 0.133322387415
                    print(f'{kpa2} kpa')
                else:
                    mmhg = float(input('How much mmhg are you converting: '))
                    kpa2 = mmhg * 0.133322387415
                    print(f'{kpa2} kpa')
            if unknown1 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG' and \
                    unknown2 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR':
                if decimal2 is str:
                    mmhg = int(input('How much mmhg are you converting?: '))
                    torr = mmhg * 1
                    print(f'{torr} torr')
                else:
                    mmhg = float(input('How much mmhg are you converting: '))
                    torr = mmhg * 1
                    print(f'{torr} torr')
            if unknown1 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG' and \
                    unknown2 in 'ATM, ATm, Atm, aTM, aTm, atM, atm':
                if decimal is str:
                    mmhg = int(input('How much mmhg are you converting?: '))
                    atm = mmhg / 760
                    print(f'{atm} atm')
                else:
                    mmhg = float(input('How much mmhg are you converting: '))
                    atm = mmhg / 760
                    print(f'{atm} atm')
            if unknown1 in 'ATM, ATm, Atm, aTM, aTm, atM, atm' and \
                    unknown2 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG':
                if decimal3 is str:
                    atm = int(input('How much atm are you converting?: '))
                    mmhg = atm * 760
                    print(f'{mmhg} mmhg')
                else:
                    atm = float(input('How much atm are you converting: '))
                    mmhg = atm * 760
                    print(f'{mmhg} mmhg')
            if unknown1 in 'ATM, ATm, Atm, aTM, aTm, atM, atm' and \
                    unknown2 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR':
                if decimal2 is str:
                    atm = int(input('How much atm are you converting?: '))
                    torr = atm * 760
                    print(f'{torr} torr')
                else:
                    atm = float(input('How much atm are you converting: '))
                    torr = atm * 760
                    print(f'{torr} torr')
            if unknown1 in 'ATM, ATm, Atm, aTM, aTm, atM, atm' and \
                    unknown2 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa':
                if decimal4 is str:
                    atm = int(input('How much atm are you converting?: '))
                    kpa2 = atm * 101.325
                    print(f'{kpa2} kpa')
                else:
                    atm = float(input('How much atm are you converting: '))
                    kpa2 = atm * 101.325
                    print(f'{kpa2} kpa')
            if unknown1 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR' and \
                    unknown2 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa':
                if decimal4 is str:
                    torr = int(input('How much torr are you converting?: '))
                    kpa2 = torr * 0.1333223684
                    print(f'{kpa2} kpa')
                else:
                    torr = float(input('How much torr are you converting: '))
                    kpa2 = torr * 0.1333223684
                    print(f'{kpa2} kpa')
            if unknown1 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR' and \
                    unknown2 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG':
                if decimal3 is str:
                    torr = int(input('How much torr are you converting?: '))
                    mmhg = torr / 1
                    print(f'{mmhg} mmhg')
                else:
                    torr = float(input('How much torr are you converting: '))
                    mmhg = torr / 1
                    print(f'{mmhg} mmhg')
            if unknown1 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR' and \
                    unknown2 in 'ATM, ATm, Atm, aTM, aTm, atM, atm':
                if decimal is str:
                    torr = int(input('How much torr are you converting?: '))
                    atm = torr / 760
                    print(f'{atm} atm')
                else:
                    torr = float(input('How much torr are you converting: '))
                    atm = torr / 760
                    print(f'{atm} atm')
        PC()


convert()
