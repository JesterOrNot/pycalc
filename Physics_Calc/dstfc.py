#! /usr/bin/python3.7
while True:
	def DSTFC():
		keywordsDist = ['d', 'dis', 'dist', 'distance']
		keywordsTime = ['t', 'tim', 'time', 'ti']
		keywordsSpeed = ['s', 'sp', 'spe', 'spee', 'speed']
		print("Welcome to the distance speed time calculator")
		solveFor = input("What are we solvig for? (distance(d), speed(s) or time(t): ").lower()
		if solveFor in keywordsDist:
			s = float(input("What is speed in meters/seconds?: "))
			t = float(input("What is the amount of time in seconds?: "))
			dist = s * t
			print("{} meters".format(dist))
		elif solveFor in keywordsTime:
			d = float(input("What is the distance in meters?: "))
			s = float(input("What is the speed in meters/seconds"))
			time = d / s
			print("{} seconds".format(time))
		elif solveFor in keywordsSpeed:
			d = float(input("What is the distance in meters?: "))
			t = float(input("What is the time in seconds"))
			speed = d / t
			print("{} m/s".format(speed))
	DSTFC()
DSTFC()