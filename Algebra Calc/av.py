import re
main = {

}
main1 = {
	
}
while True:
	def r():
		print('desired syntax: |(equ here)|')
		str1 = input('what is the equ?: ')
		equ = re.findall(r'\|.*\|', str1)
		equp2 = re.findall(r'.*', str1)
		str(equp2)
										#this takes the syntax of the equasion ie. |1 + 1| so thay it can be put through the actual equ
		z = len(equ) # this part is to verify that the syntax was correct and if it is correct updates the dict accordingly
		if z > 0:
			main.update({"equ":equ})
			main1.update({"equp2":equp2})
			pass
		else:
			print('')
			print('')
			print("SyntaxError")
			print('')
			print('')
			print('')
			print('')
			r()
	break
r()


def rc():
	# Removes excess characters
	string = main.get("equ")
	string = str(string)
	string1 = string
	string2 = string1
	char1 = "["
	char2 = "]"
	char3 = "|"
	char4 = "'"
	for i in char1:
		string = string.replace(char1, '')
	for i in char2:
		string1 = string.replace(char2, '')
	for i in char3:
		string2 = string1.replace(char3, '')
	for i in char4:
		string3 = string2.replace(char4, '')
#	string3 = float(string3)
	main1.update({"equ1":string3})
	x = main1.get("equ1")
	c = eval(x)
	z = abs(c)
	print(z)
rc()