# Division
num1 = input()
num2 = input()

try:
    num1 = int(num1)
    num2 = int(num2)
except:
    exit()

print(num1//num2)
print(num1/num2)