
sum = 0.0
count = 0
while True:
    num = input('Enter a number: ')

    if num == 'done': break

    try:
        num = int(num)
    except:
        print('Invalid Input')
        continue
    
    sum += num
    count += 1

print('After', sum, count, sum / count)