# Counting Pattern
line = input('Enter a line of text: ')

words = line.split()

print(words)

count = dict()
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)