def maxSumDivThree(nums):
    memo = {}

    def search(i, sum):
        if (i, sum) in memo:
            return memo[(i, sum)]
        if i == len(nums):
            if sum == 0:
                return 0
            else:
                return float("-inf")
        # pick
        option1 = search(i + 1, (sum + nums[i]) % 3) + nums[i]
        # not pick
        option2 = search(i + 1, sum)
        ans = max(option1, option2)
        memo[(i, sum)] = ans
        return ans

    return search(0, 0)


print(maxSumDivThree([3, 6, 5, 1, 8]))
