def two_num_sum(nums, target):
    '''
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Two Number Sum Problem
# Using Iteration method
numbers = [7, 8, 5, -4, 1, 9, 6, 3, -2]
target = 11

for val in numbers:
    print(val, end='\t')
print()

x, y = two_num_sum(numbers, target) or (0, 0)

if x + y > 0:
    print('Inside these numbers {0} + {1} is equivalent to the {2}'.format(
        numbers[x], numbers[y], target))
else:
    print('Potential match never found')
