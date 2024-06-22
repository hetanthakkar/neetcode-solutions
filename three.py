def twoSum(target, start, nums, index, res):
    left = start
    right = len(nums) - 1
    curr_sum = nums[left] + nums[right]
    while left < right:
        if curr_sum > target:
            right = right - 1
        if curr_sum < target:
            left = left + 1
        if left == right:
            return res
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            temp = [nums[left], nums[right], index]
            res.append(temp)
            left += 1
            right -= 1
    return res


def remove_duplicates(arr):
    seen = set()
    unique_arr = []
    for inner_list in arr:
        t = tuple(inner_list)
        if t not in seen:
            seen.add(t)
            unique_arr.append(inner_list)
    return unique_arr


def threeSum(nums):
    res = []
    nums.sort()
    for i in range(0, len(nums) - 1):
        remainder = -nums[i]
        twoSum(remainder, i + 1, nums, nums[i], res)
    print("res is", res)
    return remove_duplicates(res)


arr = [-1, 0, 1, 2, -1, -4]

print(threeSum(arr))
