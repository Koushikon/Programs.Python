# Parsing out the most recieved email id with how many times it apeared in the file

handle = None
try:
    handle = open('./_Files/4-mbox-short.txt')
except:
    handle = -1

count = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    count[words[1]] = count.get(words[1], 0) + 1

lst = []
for key, val in count.items():
    lst.append((val, key))

lst.sort(reverse=True)

print(lst[0][1], lst[0][0])
