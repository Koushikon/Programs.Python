number = int(input())

n1 = 0
n2 = 1
n3 = 0

for n in range(1, number):
    n3 = n1 + n2
    n1 = n2
    n2 = n3

print('Fibonacci for {} is {}'.format(number, n3))