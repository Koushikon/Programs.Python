handle = open('./_Files/4-mbox-short.txt')

for line in handle:
    line = line.rstrip()
    
    # We can use this to skip the blank line
    if line == '': continue
    word = line.split()
    
    # Or use Gradian to skip the blank lines
    # if len(word) < 1: continue
    # With Gardian a bit Stronger
    # if len(word) < 3: continue
    
    # Or Gardian in a Compound statement
    if (len(word) < 3) or (word[0] != 'From'):
        continue
    print(word[2])