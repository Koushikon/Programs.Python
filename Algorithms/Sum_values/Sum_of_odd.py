def sum_of_odd_slowONe(n):
    start = 1
    sum = 0
    for i in range(0, n):
        sum += start
        start += 2
    return sum

def sum_of_odd_fastOne(n):
    odd = 1
    return n * ((2 * odd) + (n-1) * 2) // 2


print(sum_of_odd_slowONe(5))

print(sum_of_odd_fastOne(5))