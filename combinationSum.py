def combinationSum(n, nums, target):
    if n == -1:
        return [[]]
    else:
        prev = combinationSum(n - 1, nums, target)
        for i in range(len(prev)):
            a = prev[i]
            c = nums[n]
            suma = sum(a)
            while suma + c <= target:
                a = a + [c]
                suma += c
                if a not in prev:
                    prev.append(a)
        return prev


def final(nums, target):
    temp = combinationSum(len(nums) - 1, nums, target)
    return [i for i in temp if sum(i) == target]


print(final([1, 2, 3], 4))
# print(ans)

# [[]] [1] [1,1] [1,1,1]

# prev = [[]]
# [] 2calulate sum of last elemnt of previous = 0
# while sum not exceedds target: check if sum of last element of prev plus current -> if it exceeds target than dont add to prev, else add to previous
# return prev
