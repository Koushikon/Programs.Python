# Read through the file print thw rods of that file with any duplicate words.

handle = open('./_Files/{}.txt'.format('8-romeo'))

new = list()
count = 0
for lines in handle:
    lines = lines.rstrip()
    lst = lines.split()
    for words in lst:
        if words in new: continue
        new.append(words)
            
print(sorted(new))