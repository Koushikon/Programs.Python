# Assignment 3.1
hours = input('Enter the hour? ')
rate = input('Enter rate of per hour? ')

try:
    hours = int(hours)
    rate = float(rate)
except:
    print('Enter numeric for Hours and float for Rate.')
    quit()

normal_hour = 40

if hours <= normal_hour:
    total_rate = hours * rate
else:
    hours = ((hours - normal_hour) * 1.5) * rate
    total_rate = (normal_hour * rate) + hours

print('Pay:', total_rate)