# Arithmetic Operators
num1 = input()
num2 = input()

try:
    num1 = int(num1)
    num2 = int(num2)
except:
    exit()

if (num1 >= 1 and num1 <= 10**10) and (num2 >= 1 and num2 <= 10**10):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)