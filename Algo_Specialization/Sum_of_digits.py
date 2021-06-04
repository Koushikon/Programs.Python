# num1 = input('Enter the 1st No. ')
# num2 = input('Enter the 2nd No. ')
# Or do this in one line.
num1, num2 = input('Enter two numbersby sapce: ').split()

try:
    num1 = int(num1)
    num2 = int(num2)
except:
    num1 = num2 = -1
    # quit()

if num1 > 0:
    print(num1+num2)
    # print('First number is {} and the second number is {}, Sum: '.format(num1, num2),(num1+num2))
else:
    print('Error, Please enter numeric input.')