import os
print("Welcome to misc calcs this is just a bunch of handy little calcs that couldn't be placed in other catogories but I still thought might be useful to someone enjoy the available calcultaors are: Gpa calc(gpa)")
def choose():
    usrInt = input("What Calc do you want?: ").lower()
    if usrInt in 'gpa':
        import misc.gpa
    else:
        print("An error has occured\nPlease try again")
choose()
