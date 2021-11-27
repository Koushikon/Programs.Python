def two_num_sum(nums, target):
    '''
    Time Complexity: O(nlogn)
    Space Complexity: O(1)
    '''

    # Sorting the numbers with Python Built-in Sorting algorithm
    # Most Optimul sorting algorith's in O(logn) time
    nums.sort()

    # Now Find the matching part in O(n) time
    left = 0
    right = len(nums) - 1
    for _ in range(len(nums)):
        join_value = nums[left] + nums[right]
        if join_value > target:
            right -= 1
        elif join_value < target:
            left += 1
        else:
            return [left, right]
    return []


# Two Number Sum Problem
# Using First a Sorting algorithm
# Then Find the matching with 2 Moving Pointers Left and Right
numbers = [7, 8, 5, -4, 1, 9, 6, -2]
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
