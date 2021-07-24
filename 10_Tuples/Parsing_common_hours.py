# Parsing hour from a text time and show the most common hourse

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
    
    # We could use this way
    # hour = words[5].split(':')
    # count[hour[0]] = count.get(hour[0], 0) + 1
    
    # Or we could use this way
    end_of_hour = words[5].find(':')
    hour = words[5][:end_of_hour]
    count[hour] = count.get(hour, 0) + 1
    

for key, value in sorted(count.items()):
    print(key, value)


