def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input())

print('Fibonacci for {} is {}'.format(number, fibonacci(number)))