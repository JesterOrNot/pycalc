def displace():
    initial=float(input("What is the initial?: "))
    final=float(input("What is the final?: "))
    magnitude=final-initial
    magnitudeStr = str(magnitude)
    if magnitude > 0:
        print("The awnser is: " + '+ ' + magnitudeStr)
    else:
        magnitudeStr=magnitudeStr.replace('-','- ').replace("'","")
        print("The awnser is: " + magnitudeStr)
displace()
