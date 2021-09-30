def fizzbuzz(fst, n):
    for x in range (fst, n + 1):
        message = ''
        if x % 3 ==0:
            message += 'Fizz'
        if x % 5 == 0:
            message += 'Buzz'
        print(x if not message else message)

fizzbuzz(1, 100)