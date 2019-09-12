#! /usr/bin/python3.7
def convert():
    convertorno = input('Do we need to convert?: ')
    if convertorno in 'yes, Yes, yEs, yeS, yES, YES, YEs, YEs, y':
        uc()
        convert()
    elif convertorno in 'no, No, nO, NO,n':
        CGL()
def CGL():
    unknown = input('What is the unknown Variable P1,V1,T1,P2,V2,T2: ')
    if unknown in 'P1,p1':
        v1 = float(input('What is the initial volume in Liters: '))
        v2 = float(input('What is the volume after in Liters: '))
        t1 = float(input('What is th initial Temperature in Kelvin: '))
        t2 = float(input('What is the temperature after in K: '))
        p2 = float(input('What is the pressure after in atm: '))
        p1 = p2 * v2 * t1 / (t2 * v1)
        print('P1 = {} atm'.format(p1))
    if unknown in 'P2,p2':
        t1 = float(input('What is th initial Temperature in Kelvin: '))
        t2 = float(input('What is the temperature after in K: '))
        v1 = float(input('What is the initial volume in Liters'))
        v2 = float(input('What is the volume after in Liters: '))
        p1 = float(input('What is the initial pressure in atm: '))
        p2 = p1 * v1 * t2 / (t1 * v2)
        print('P2 = {} atm'.format(p2))
    if unknown in 'V1,v1':
        p1 = float(input('What is the initial pressure in atm: '))
        p2 = float(input('What is the pressure after in atm: '))
        t1 = float(input('What is th initial Temperature in Kelvin: '))
        t2 = float(input('What is the temperature after in K: '))
        v2 = float(input('What is the volume after in Liters: '))
        v1 = p2 * v2 * t1 / (t2 * p1)
        print('V1 = {} liters'.format(v1))
    if unknown in 'V2,v2':
        p1 = float(input('What is the initial pressure in atm: '))
        p2 = float(input('What is the pressure after in atm: '))
        t1 = float(input('What is th initial Tempters in Kelvin: '))
        t2 = float(input('What is the temperature after in K: '))
        v1 = float(input('What is the initial volume in Liters: '))
        v2 = p1 * t2 * v1 / (p2 * t1)
        print('V2 = {} liters'.format(v2))
    if unknown in 'T1,t1':
        p1 = float(input('What is the initial pressure in atm: '))
        p2 = float(input('What is the pressure after in atm: '))
        v1 = float(input('What is th initial volume in Liters: '))
        v2 = float(input('What is the volume after in Liters: '))
        t2 = float(input('What is the temperature after in K: '))
        t1 = p1 * v1 * t2 / (p2 * v2)
        print('T1 = {} kelvin'.format(t1))
    if unknown in 'T2,t2':
        p1 = float(input('What is the initial pressure in atm: '))
        p2 = float(input('What is the pressure after in atm: '))
        t1 = float(input('What is th initial Temperature in Kelvin: '))
        v2 = float(input('What is the volume after in Liters: '))
        v1 = float(input('What is the initial volume in Liters: '))
        t2 = p2 * t1 * v2 / (p1 * v1)
        print('T2 = {} kelvin'.format(t2))
def uc():
    unknown = input('What Are we converting to Temperature or pressure: ')
    if unknown in 'temp, Temperature, temperature, t':
        def TC():
            c = 0
            decimal = c
            f = 0
            decimal2 = f
            k = 0
            decimal3 = k
            unknown1 = input(
                'What is the starting temp in, C, K or F: ')
            unknown2 = input(
                'What are we converting to, C, K or F: ')
            if unknown1 in 'C, c' and \
               unknown2 in 'F, f':
                if decimal2 is str:
                    c = int(input('What is the starting temp in c that you are converting?: '))
                    f = c * 1.8000 + 32
                    print('{} °F'.format(f))
                else:
                    c = float(input('What is the starting temp in c that you are converting?: '))
                    f = c * 1.8000 + 32
                    print('{} °F'.format(f))
            if unknown1 in 'C, c' and \
               unknown2 in 'K, k':
                if decimal3 is str:
                    c = int(input('What is the starting temp in c that you are converting?: '))
                    k = c + 273
                    print('{} °K'.format(k))
                else:
                    c = float(input('What is the starting temp in c that you are converting?: '))
                    k = c + 273
                    print('{} °K'.format(k))
            if unknown1 in 'K, k' and \
               unknown2 in 'F, f':
                if decimal2 is str:
                    k = int(input('What is the starting temp in k that you are converting?: '))
                    f = k * 1.8 - 459.67
                    print('{} °F'.format(f))
                else:
                    k = float(input('What is the starting temp in k that you are converting?: '))
                    f = k * 1.8 - 459.67
                    print('{} °F'.format(f))
            if unknown1 in 'K, k' and \
               unknown2 in 'C, c':
                if decimal is str:
                    k = int(input('What is the starting temp in k that you are converting?: '))
                    c = k - 273
                    print('{} °C'.format(c))
                else:
                    k = float(input('What is the starting temp in k that you are converting?: '))
                    c = k - 273
                    print('{} °C'.format(c))
            if unknown1 in 'F, f' and \
               unknown2 in 'K, k':
                if decimal3 is str:
                    f = int(input('What is the starting temp in k that you are converting?: '))
                    k = ((f - 32)/1.8)+273/15
                    print('{} °K'.format(k))
                else:
                    f = float(input('What is the starting temp in k that you are converting?: '))
                    k = ((f - 32)/1.8)+273/15
                    print('{} °K'.format(k))
            if unknown1 in 'F, f' and \
               unknown2 in 'C, c':
                if decimal is str:
                    f = int(input('What is the starting temp in f that you are converting?: '))
                    c = (f - 32)/1.8
                    print('{} °C'.format(c))
                else:
                    f = float(input('What is the starting temp in f that you are converting?: '))
                    c = (f - 32)/1.8
                    print('{} °C'.format(c))
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
                    print('{} atm'.format(atm))
            if unknown1 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa ' and \
            unknown2 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR':
                if decimal2 is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    torr = kpa / 101.3
                    print('{} torr'.format(torr))
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    torr = kpa / 0.1333223684
                    print('{} torr'.format(torr))
            if unknown1 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa ' and \
            unknown2 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG':
                if decimal3 is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    mmhg = kpa / 0.1333223684
                    print('{} mmhg'.format(mmhg))
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    mmhg = kpa / 0.1333223684
                    print('{} mmhg'.format(mmhg))
            if unknown1 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG' and \
            unknown2 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa' :
                if decimal4 is str:
                    mmhg = int(input('How much mmhg are you converting?: '))
                    kpa2 = mmhg * 0.133322387415
                    print('{} kpa'.format(kpa2))
                else:
                    mmhg = float(input('How much mmhg are you converting: '))
                    kpa2 = mmhg * 0.133322387415
                    print('{} kpa'.format(kpa2))
            if unknown1 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG' and \
            unknown2 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR' :
                if decimal2 is str:
                    mmhg = int(input('How much mmhg are you converting?: '))
                    torr = mmhg * 1
                    print('{} torr'.format(torr))
                else:
                    mmhg = float(input('How much mmhg are you converting: '))
                    torr = mmhg * 1
                    print('{} torr'.format(torr))
            if unknown1 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG' and \
            unknown2 in 'ATM, ATm, Atm, aTM, aTm, atM, atm' :
                if decimal is str:
                    mmhg = int(input('How much mmhg are you converting?: '))
                    atm = mmhg / 760
                    print('{} atm'.format(atm))
                else:
                    mmhg = float(input('How much mmhg are you converting: '))
                    atm = mmhg / 760
                    print('{} atm'.format(atm))
            if unknown1 in 'ATM, ATm, Atm, aTM, aTm, atM, atm' and \
            unknown2 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG' :
                if decimal3 is str:
                    atm = int(input('How much atm are you converting?: '))
                    mmhg = atm * 760
                    print('{} mmhg'.format(mmhg))
                else:
                    atm = float(input('How much atm are you converting: '))
                    mmhg = atm * 760
                    print('{} mmhg'.format(mmhg))
            if unknown1 in 'ATM, ATm, Atm, aTM, aTm, atM, atm' and \
            unknown2 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR':
                if decimal2 is str:
                    atm = int(input('How much atm are you converting?: '))
                    torr = atm * 760
                    print('{} torr'.format(torr))
                else:
                    atm = float(input('How much atm are you converting: '))
                    torr = atm * 760
                    print('{} torr'.format(torr))
            if unknown1 in 'ATM, ATm, Atm, aTM, aTm, atM, atm' and \
            unknown2 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa':
                if decimal4 is str:
                    atm = int(input('How much atm are you converting?: '))
                    kpa2 = atm * 101.325
                    print('{} kpa'.format(kpa2))
                else:
                    atm = float(input('How much atm are you converting: '))
                    kpa2 = atm * 101.325
                    print('{} kpa'.format(kpa2))
            if unknown1 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR' and \
            unknown2 in 'KPA, KPa, Kpa,kPA, kPa, kpA, kpa':
                if decimal4 is str:
                    torr = int(input('How much torr are you converting?: '))
                    kpa2 = torr * 0.1333223684
                    print('{} kpa'.format(kpa2))
                else:
                    torr = float(input('How much torr are you converting: '))
                    kpa2 = torr * 0.1333223684
                    print('{} kpa'.format(kpa2))
            if unknown1 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR' and \
            unknown2 in 'MMHG, MMHg, MMhg, Mmhg, mMHG, mmHg, mMhg, mmhg, mmhG':
                if decimal3 is str:
                    torr = int(input('How much torr are you converting?: '))
                    mmhg = torr / 1
                    print('{} mmhg'.format(mmhg))
                else:
                    torr = float(input('How much torr are you converting: '))
                    mmhg = torr / 1
                    print('{} mmhg'.format(mmhg))
            if unknown1 in 'TORR, TORr, TOrr, Torr, tORR, tORr, tOrr, torr, torR' and \
            unknown2 in 'ATM, ATm, Atm, aTM, aTm, atM, atm':
                if decimal is str:
                    torr = int(input('How much torr are you converting?: '))
                    atm = torr / 760
                    print('{} atm'.format(atm))
                else:
                    torr = float(input('How much torr are you converting: '))
                    atm = torr / 760
                    print('{} atm'.format(atm))
        PC()
convert()
