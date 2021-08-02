import re

try:
    handle = open('./_Files/4-mbox-short.txt')
except:
    exit()

lst = list()
for lines in handle:
    lines = lines.rstrip()
    # Looking for real numbers in line like 0.7002, Then extract them out
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', lines)
    if len(stuff) != 1: continue
    lst.append(float(stuff[0]))
    
    
print('Maximum: ', max(lst))


# print('Average spam confidence:', addition/count)