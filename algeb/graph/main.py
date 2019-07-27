print('Welcome to the graphing calculator the only option so far is graphing quadratic models(qe), exponential functions(ef)')
userInt = input("What do you want to graph?: ")

def choose():
    if userInt in 'qe':
        import algeb.graph.graphQuadMod
    elif userInt in 'ef':
        import algeb.graph.graphExpFunc
    else:
        print("Error, Please try again this error may be due to mispelling on your part")
        choose()
choose()
