hours = input('Enter the hour? ')
rate = input('Enter rate of per hour? ')

try:
    hours = int(hours)
    rate = float(rate)
except:
    print('Enter numeric for Hours and float for Rate.')
    quit()

total_rate = hours * rate

print('Pay:', total_rate)