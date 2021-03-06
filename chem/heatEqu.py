#! /usr/bin/python3


def HE():
    q = 0
    decimal1 = q
    m = 0
    decimal2 = m
    c = 0
    decimal3 = c
    fi = 0
    decimal4 = fi
    ini = 0
    decimal5 = ini
    dt = 0
    s = input('What are we solving for? (q, m, c or ΔT): ').lower()
    if s == "q":
        if decimal2 is str:
            m = int(input('What is the mass in grams(m): '))
        else:
             m = float(input('What is the mass in grams(m): '))
        if decimal4 is str:
            fi = int(input('What is the final temperature in °C(ΔT): '))
        else:
            fi = float(input('What is the final temperature in °C(ΔT): '))
        if decimal5 is str:
            ini = int(input('What is the initial temperature in °C(ΔT): '))
        else:
            ini = float(input('What is the initial temperature in °C(ΔT): '))
        if decimal3 is str:
            c = int(input('What is the specific heat? (c): '))
        else:
            c = float(input('What is the specific heat? (c): '))
        q = m * c*(fi - ini)
        print(f'q = {q}J')
    elif s == 'm':
        if decimal1 is str:
            q = int(input('What is the amount of heat in joules(q): '))
        else:
            q = float(input('What is the amount of heat in joules(q): '))
        if decimal4 is str:
            fi = int(input('What is the final temperature in °C(ΔT): '))
        else:
            fi = float(input('What is the final temperature in °C(ΔT): '))
        if decimal5 is str:
            ini = int(input('What is the initial temperature in °C(ΔT): '))
        else:
            ini = float(input('What is the initial temperature in °C(ΔT): '))
        if decimal3 is str:
            c = int(input('What is the specific heat? (c): '))
        else:
            c = float(input('What is the specific heat? (c): '))
        m = q/(c*(fi - ini))
        print('m = {m}g')
    elif s == 'c':
        if decimal1 is str:
            q = int(input('What is the amount of heat in joules(m): '))
        else:
            q = float(input('What is the amount of heat in joules(q): '))
        if decimal4 is str:
            fi = int(input('What is the final temperature? (c): '))
        else:
            c = float(input('What is the final temperature? (c): '))
        if decimal5 is str:
            ini = int(input('What is the initial temperature (c)'))
        else:
            ini = float(input('What is the initial temperature (c):'))
        if decimal2 is str:
           m = int(input('What is the mass in grams(m): '))
        else:
          m = float(input('What is the mass in grams(m): '))
        c = q/((fi-ini)*m)
        print('c = {c}J/°C')
    elif s == 't':
      if decimal1 is str:
        q = int(input('What is the amount of heat in Joules (q): '))
      else:
        q = float(input('What is the amount of heat in Joules (q): '))
      if decimal2 is str:
        m = int(input('What is the mass in grams(m): '))
      else:
        m = float(input('What is the mass in grams(m): '))
      if decimal3 is str:
        c = int(input('What is the specific heat? (c): '))
      else:
        c = int(input('What is the specific heat (c): '))
      dt = q/(c*m)
      print('ΔT = {dt}°C')
def convert():
    convert_or_no = input('Do we need to convert?: ').lower()
    if convert_or_no in 'yes, Yes, yEs, yeS, yES, YES, YEs, YEs, y':
        uc()
        convert()
    elif convert_or_no in 'no, No, nO, NO,n':
        HE()
def uc():
    unknown = input('What Are we converting to temperature or pressure: ')
    if unknown in 'temp, temperature, temperature, t':
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
            unknown1 = input('What are we starting with? (Kpa, Atm, Torr,Mmhg): ').lower()
            unknown2 = input('What are we converting to? (Kpa, Atm, Torr,Mmhg): ').lower()
            if unknown1 == 'kpa' and \
              unknown2 == 'atm':
                if decimal is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    atm = kpa / 101.325
                    print(f'{atm} atm')
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    atm = kpa / 101.325
                    print(f'{atm} atm')
            if unknown1 == 'kpa' and \
            unknown2 == 'torr':
                if decimal2 is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    torr = kpa / 101.3
                    print(f'{torr} torr')
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    torr = kpa / 0.1333223684
                    print(f'{torr} torr')
            if unknown1 == 'kpa ' and \
            unknown2 == 'mmhg':
                if decimal3 is str:
                    kpa = int(input('How much kpa are you converting?: '))
                    mmhg = kpa / 0.1333223684
                    print(f'{mmhg} mmhg')
                else:
                    kpa = float(input('How much kpa are you converting: '))
                    mmhg = kpa / 0.1333223684
                    print(f'{mmhg} mmhg')
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