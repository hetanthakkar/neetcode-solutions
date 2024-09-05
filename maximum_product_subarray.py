def main(nums):
    dp = {}

    def max_product_subarray(i):
        if dp[i]:
            return dp[i]
        if i == 0:
            dp[i] = [nums[0], nums[0]]
            return [nums[0], nums[0]]
        prev = max_product_subarray(i - 1)
        ans1 = min(nums[i], prev[0] * nums[i], prev[1] * nums[i])
        ans2 = max(nums[i], prev[0] * nums[i], prev[1] * nums[i])
        dp[i] = [ans1, ans2]
        return [ans1, ans2]

    maximum_prod = float("-inf")
    for i in range(0, len(nums)):
        maximum_prod = max(maximum_prod, max_product_subarray(i)[1])
    return maximum_prod


print(main([-2, 3, -4]))
