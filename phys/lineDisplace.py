def displace():
    initial=float(input("What is the initial?: "))
    final=float(input("What is the final?: "))
    magnitude=final-initial
    magnitudeStr = str(magnitude)
    if magnitude > 0:
        print('+ ' + magnitudeStr)
    else:
        magnitudeStr=magnitudeStr.replace('-','- ').replace("'","")
        print(magnitudeStr)
displace()
