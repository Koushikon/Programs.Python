# Print out the recieved mail id's and total number of mails

handle = open('./_Files/{}.txt'.format('4-mbox-short'))

count = 0
e_lst = list()
for lines in handle:
    if not lines.startswith('From '): continue
    lines = lines.rstrip()
    lst = lines.split()
    print(lst[1])
    count += 1

print('There were {} lines in the file with From as the first word'.format(count))