import math


def findLongestChain(nums):
    nums = sorted(nums, key=lambda x: math.sqrt((x[1] * x[1] + x[0] * x[0])))
    print(nums)

    def search(current):
        maxi = 0
        if current == 0:
            return 1
        for i in range(current - 1, -1, -1):
            option1 = 0
            if nums[current][0] > nums[i][0] and nums[current][1] > nums[i][1]:
                option1 = 1 + search(i)
            option2 = search(i - 1)
            maxi = max(maxi, max(option1, option2))

        return maxi

    max_len = 0
    for i in range(0, len(nums)):
        max_len = max(max_len, search(i))
    return max_len


print(findLongestChain([[17, 15], [17, 18], [2, 8], [7, 2], [17, 2], [17, 8], [6, 15]]))
