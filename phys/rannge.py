import math
def range():
    v0 = float(input("What is the initial velocity?: "))
    theta = float(input("What is the theta?: "))
    gravity = float(input("What is the gravity?: "))
    equ = v0**2*math.sin(2*theta)/(2*gravity)
    print(equ)
range()