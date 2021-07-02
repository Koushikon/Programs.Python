# Read through a file and print contents line byline in upper case
file_name = 'None'

def getting_file():
    f_name = input('Enter file name: ')
    return f_name

while True:
    file_name = getting_file()
    
    try:
        handle = open(file_name)
    except:
        handle = -1
        print('\tWrong filename {} Please, Try again'.format(file_name))
        continue

    if handle != -1:
        break

for lines in handle:
    lines = lines.rstrip()
    print(lines.upper())