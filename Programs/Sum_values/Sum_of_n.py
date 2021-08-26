# Sum of n natural number

def slow_formula(n):
    sum = 0
    for number in range(1, n+1):
        sum += number
    return sum

def fast_formula(n):
    return (n * (n+1))//2

number = int(input())

slowOne = slow_formula(number)
fastOne = fast_formula(number)

print('Sum of {} number is {}'.format(number, slowOne))

print('Sum of {} number is {}'.format(number, fastOne))

print('They both are same it\'s', (slowOne ==fastOne))
