def max_pairwise_product(nums):
    product = 0
    size = len(nums)
    for val in range(size-1):
        for val2 in range(val+1 , size):
            # product = max(nums[val] * nums[val2], product)
            if (nums[val] * nums[val2]) > product: product = nums[val] * nums[val2]
    return product


size = int(input())
lst = list()
for val in range(size):
    lst.append(int(input()))

print(max_pairwise_product(lst))