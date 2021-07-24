# Print the number as float values

text = "X-DSPAM-Confidence:    0.8475"

# This way
pos = text.find('0')
val = text[pos:len(text)+1]
print(float(val))

# Or, this way
pos = text.find(':')
val = text[pos+1:]
val = float(val.strip())
print(val)

# Or, this way
lst = text.split()
print(float(lst[1]))