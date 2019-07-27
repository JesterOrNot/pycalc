#! /usr/bin/python3.7

print("Welcome to the area finder the shapes that this can find the area for so far are trapazoid(Trap), area of triangle (tri), area of circle(circ)")

def asp():
    userInt = input('What do you want to find the area of?: ').lower()
    if userInt == 'trap':
        import geom.area.AOTrap
    elif userInt == 'tri':
        import geom.area.AOTriangle
    elif userInt == 'circ':
        import geom.area.AOCircle
    elif userInt == 'exit':
        exit()
    else:
        print("An error has occured")
    asp()
asp()
