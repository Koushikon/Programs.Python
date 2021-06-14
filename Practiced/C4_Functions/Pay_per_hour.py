# Assignment 4.6
hours = input('Enter the hour? ')
rate = input('Enter rate of per hour? ')

try:
    hours = int(hours)
    rate = float(rate)
except:
    print('Enter numeric for Hours and float for Rate.')
    quit()

def computepay(h, r):
    normal_hour = 40
    if h <= normal_hour:
        return h * r
    else:
        h = ((h - normal_hour) * 1.5) * r
        return (normal_hour * rate) + h

print('Pay:', computepay(hours, rate))