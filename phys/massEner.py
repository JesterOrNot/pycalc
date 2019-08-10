def me():
    m = float(input("What is the mass? in kg: "))
    c = float(input("What is the speed of light in a vacuum in m/s?: "))
    c2 = c**2
    e = m*c2
    print(f"E = {e}j")
me()