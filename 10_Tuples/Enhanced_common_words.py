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

# using list comprehension
lst = sorted([(v, k) for k, v in count.items()], reverse=True)
print(lst[:5])

# Or More compact way using list comprehension
print(sorted([(v, k) for k, v in count.items()], reverse=True))