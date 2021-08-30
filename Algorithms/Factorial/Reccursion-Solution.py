# Factorial number using reccursion

def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n-1)

print(factorial(15))