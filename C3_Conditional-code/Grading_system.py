sub = input('Enter the Subject name? ')
marks = input('Enter the marks? ')

try:
    marks = int(marks)
except:
    print("Error, You've entered Non-numeric value." )
    quit()

if marks < 0 or marks > 100:
    print('Enter marks between 0 to 100.')
    quit()
elif marks >= 0 and marks < 40: grade = 'F'
elif marks >= 40 and marks < 60: grade = 'C'
elif marks >= 60 and marks < 80: grade = 'B'
elif marks >= 80 and marks < 90: grade = 'A'
else: grade = 'A++'

print('Your {} marks is: {} and grade is: {}'.format(sub, marks, grade))