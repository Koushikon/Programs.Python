# Sum of n natural number

def slow_formula(n):
    start = 2
    sum = 0
    for number in range(n):
        sum += start
        start += 2
    return sum

def fast_formula(n):
    even = 2
    return (n * (2 * even + (n - 1) * 2)) // 2

number = int(input())

slowOne = slow_formula(number)
fastOne = fast_formula(number)

print('Sum of {} even number is {}'.format(number, slowOne))

print('Sum of {} even number is {}'.format(number, fastOne))

print('They both are same it\'s', (slowOne ==fastOne))
