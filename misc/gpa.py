values = {
        "A+": 4.33,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.33,
        "B": 3,
        "B-": 2.7,
        "C+": 2.33,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.33,
        "D": 1,
        "D-": 0.7,
        "F": 0,
        }


def gpa():
    c = 0
    while c == 0:  # For the infinite loop
        x = int(input('How grades do you have?:  '))  # This sets a limit
        x = x - 1  # this is to account for the computers understanding that 0 is included in the number's value
        r = []  # helps maintain the limit
        while len(r) <= x:  # same with this one
            m = input('Input a grade: ').upper()
            if m in values:  # if the grade input by the user is n the table it adds that corresponding value to the list
                r.append(values[m])
            else:
                print('Sorry yum must have mistyped something. Please try again :(')
        sum_of_num = sum(r)  # the equation for gpa is sum/length this takes the sum of the list we made and stores it in a variable
        length = len(r)  # this takes the length of the list and once again stores it in a variable
        gpa = sum_of_num / length  # this is the actual equ
        print(f'Your gpa is {gpa}')
        break


gpa()
