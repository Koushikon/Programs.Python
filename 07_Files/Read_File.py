# Read through the file and print all lines with uppercase letters

f_name = input();

try:
    handle = open('./_Files/{}.txt'.format(f_name))
except:
    handle = -1
    exit()

for lines in handle:
    lines = lines.rstrip()
    print(lines.upper())