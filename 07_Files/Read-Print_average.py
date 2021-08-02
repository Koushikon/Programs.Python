# Read throught the file extract the number from this "X-DSPAM-Confidence:    0.8475" string and print the average of the numbers.

f_name = input();

try:
    handle = open('./_Files/{}.txt'.format(f_name))
except:
    handle = -1
    exit()

addition = count = 0
lst = list()
for lines in handle:
    if not lines.startswith('X-DSPAM-Confidence:'):
        continue
    pos = lines.find(':')
    lst = lines[pos + 1:].strip()
    addition += float(lst)
    count += 1

print('Average spam confidence:', addition/count)