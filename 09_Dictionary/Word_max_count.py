# Access the file data check for most common word and its count then print them

# Checking file status
def check_file(name):
    try:
        file_temp = open('./_Files/{}.txt'.format(name))
    except:
        print('\tWrong filename, Try again.')
        file_temp = None
    return file_temp

# Repeating asking file name
while True:
    name = input('Enter file name: ')

    if len(name) < 1: name = '6-clown.txt'
    elif name.lower() == 'done': exit()
    
    handle = check_file(name)

    if handle is None: continue
    else: break

# Checking file Data
count = dict()
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

# Calculating Most common word and its count
bigword = None
bigcount = 0
for key, val in count.items():
    if val > bigcount:
        bigword = key
        bigcount = val

print('\t🎊 Most common word is "{}" appear "{}" times.'.format(bigword, bigcount))