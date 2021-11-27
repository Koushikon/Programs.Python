def two_num_sum(nums, target):
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    value = {}
    for x in nums:
        y = target - x
        if y in value:
            return [x, y]
        else:
            value[x] = True
    return []


# Two Number Sum Problem
# Using Hash Table Technique
numbers = [7, 8, 5, -4, 1, 9, 6, -2]
target = 11

for val in numbers:
    print(val, end='\t')
print()

x, y = two_num_sum(numbers, target) or (0, 0)

if x + y > 0:
    print(f'Inside these numbers {x} + {y} is equivalent to the {target}')
else:
    print('Potential match never found')
