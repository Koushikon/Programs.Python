# Taking file path
def file_open(fnm):
    try:
        hdl = open('./_Files/{}.txt'.format(fnm))
    except:
        print('\tWrong filename, Try again.')
        hdl = None
    return hdl

# Handling file
while True:
    fname = input('Enter the file name only: ')
    
    if len(fname) < 1: fname = '6-clown'
    elif fname.lower() == 'done': exit()
    print(fname)
    handle = file_open(fname)

    if handle == None: continue
    else: break

# Creates dictionary and count the words apear how many times
count = dict()
for lines in handle:
    lines = lines.rstrip()
    words = lines.split()
    for word in words:
        count[word] = count.get(word, 0) + 1

# create an temporary list and assign it to value and key order
lst = list()
for key, val in count.items():
    lst.append((val, key))

# sorting the list
# lst = sorted(lst, reverse=True)
lst.sort(reverse=True)

# We could print it like this
# print(lst[:5])

for key, val in lst[:5]:
    print(val, key)

# To print all
# print(lst)
