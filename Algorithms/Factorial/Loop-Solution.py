# Factorial number using loop

def factorial(n):
    total = n
    for i in range(1, n):
        total *= (n - i)
    return total


print(factorial(15))