print('Welcome to the graphing calculator the only option so far is graphing quadratic models(qe)')
userInt = input("What do you want to graph?: ")
def choose():
    if userInt in 'qe':
        import quadratic_Models
choose()