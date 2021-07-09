sub = input('Enter the Subject name? ')
marks = input('Enter the marks? ')

try:
    marks = int(marks)
except:
    print("Error, You've entered Non-numeric value." )
    quit()


def grade_cal(f_marks):
    if f_marks < 0 or f_marks > 100:
        print('Enter f_marks between 0 to 100.')
        quit()
    elif f_marks >= 0 and f_marks < 40: return 'F'
    elif f_marks >= 40 and f_marks < 60: return 'C'
    elif f_marks >= 60 and f_marks < 80: return 'B'
    elif f_marks >= 80 and f_marks < 90: return 'A'
    else: return 'A++'

print('Your {} marks is: {} and grade is: {}'.format(sub, marks, grade_cal(marks)))