def displace():
    x1=float(input("What is x1: "))
    x2=float(input("What is x2: "))
    Δx=x2-x1
    Δx_str = str(Δx)
    if Δx > 0:
        print("Δx = " + '+ ' + Δx_str)
    else:
        Δx_str=Δx_str.replace('-','- ').replace("'","")
        print("Δx = " + Δx_str)
displace()
