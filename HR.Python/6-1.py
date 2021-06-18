# Write a function
def is_leap(year):
    if (year >= 1900 and year <= 10**5):
        if (year % 100) == 0:
            year //= 100
        else:
            year %= 100
        if (year % 4) == 0:
            return True
        else:
            return False
    else:
        exit()

year = input()

try:
    year = int(year)
except:
    exit()

print(is_leap(year))