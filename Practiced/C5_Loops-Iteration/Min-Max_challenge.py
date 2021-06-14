# Assignment 5.2

def max_num(num, big):
    if num > big:
        return num
    return big

def min_num(num, tiny):
    if num < tiny:
        return num
    return tiny

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    if largest == None and smallest == None : largest = smallest = num

    largest = max_num(num, largest)
    smallest = min_num(num, smallest)

print("Maximum is", largest)
print("Minimum is", smallest)