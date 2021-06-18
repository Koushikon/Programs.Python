# Loops
num1 = input()

try:
    num1 = int(num1)
except:
    exit()

iterate = 0
if num1 >= 1 and num1 <= 20:
    while iterate < num1:
        print(iterate**2)
        iterate += 1