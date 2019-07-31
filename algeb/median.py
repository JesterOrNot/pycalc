def median3():
    numbers1 = input("What numbers are we finding the median of?: ")
    numbers1 = numbers1.split(",")
    num = []
    for i in numbers1:
        i = float(i)
        n = num.append(i)
    n1 = num.sort()
    z = len(num)
    if z % 2 == 0:
        median1 = num[z//2]
        median2 = num[z//2-1]
        median = (median1 + median2)/2
    else:
        median = num[z//2]
        median = float(median)
    print(f"The Median is: {median}")
median3()
