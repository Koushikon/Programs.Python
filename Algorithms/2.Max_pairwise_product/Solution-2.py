def max_pairwise_product(nums):
    size = len(nums)
    max1= -1
    for i in range(size):
        if max1 == -1 or nums[i] > nums[max1]:
            max1 = i

    max2 = -1
    for j in range(size):
        if max1 != j and (max2 == -1 or nums[j] > nums[max2]):
            max2 = j
    return nums[max1]* nums[max2]

size = int(input())

numbers = list()
while size > 0:
    numbers.append(int(input()))
    size -= 1

print(max_pairwise_product(numbers))