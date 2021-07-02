# Counting lines that starts with "Subject:"

file_name = 'None'

def getting_file_name():
    file_n = input('Enter file name: ')
    return file_n

while True:
    try:
        file_name = getting_file_name()
        handle = open(file_name)
    except:
        handle = -1
        print('\tWrong file name {}, Try again'.format(file_name))
        continue

    if handle != -1:
        break
        
count = 0
for line in handle:
    if line.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', file_name)
handle.close()