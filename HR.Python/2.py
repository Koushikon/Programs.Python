number = input()

try:
    number = int(number)
except:
    number = -1

if number >= 1 and number <= 100:
    if (number % 2) == 1: print('Weird')
    else:
        if  (number >= 2 and number <= 5) or number > 20 : print('Not Weird')
        else:
            print('Weird')
else:
    exit()