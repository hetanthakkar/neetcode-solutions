def houseRobber(nums):
    def search(end):
        if end == 0:
            return nums[0]
        if end < 0:
            return 0
        maxi = max(search(end - 2) + nums[end], search(end - 1))
        return maxi

    maximum = float("-inf")
    for i in range(len(nums)):
        maximum = max(maximum, search(i))

    return maximum


print(houseRobber([2, 7, 9, 3, 1]))
