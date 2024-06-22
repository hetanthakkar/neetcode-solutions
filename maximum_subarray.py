def maximum_subarray(nums):
    negative = True
    for num in nums:
        if num > 0:
            negative = False
    if negative:
        return max(nums)
    max_sum = 0
    current_sum = 0
    for num in nums:
        if num + current_sum > current_sum:
            max_sum = max(current_sum, max_sum)
            current_sum = num + current_sum
        else:
            current_sum += num
    return max_sum


# [1, -2, 3]
# 2,1,-3,4

print(maximum_subarray([1, -1, 1]))
# maximum_subarray([2, 1, -3, 4, -10, 99])

# left+right>0
# calculate sum from start till negative, if that sum is positive and suffix sum is also positive then include the element
