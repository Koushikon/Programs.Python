# How to merge two dictionaries
# In Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)

# In Python 2.x you could
# Use this:
z = dict(x, **y)

print(z)

# In these examples, Python mergers dictionary keys
# in the order listed in the expression, over writing
# duplicates from left to right