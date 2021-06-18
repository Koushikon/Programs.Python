# Print Function
def printing(iterate):
    str_number = ''
    number = 1
    while iterate > 0:
        str_number += str(number)
        iterate -= 1
        number += 1
    return str_number

iterate = input()

try:
    iterate = int(iterate)
except:
    exit()

if iterate >= 1 and iterate <= 150:
    print(printing(iterate))