def sliding_window_maximum(nums, k):
    s2_max = max(nums[1 : k + 1])
    s1_max = max(nums[0:k])
    s1 = [s1_max]
    s2 = []
    res = [s1_max]
    for i in range(1, len(nums) - k + 1):
        s2_max = max(s2_max, nums[i + k - 1])
        s2.append(s2_max)

    for i in range(0, len(nums) - k):
        s1_max = max(s1_max, nums[i + k])
        s1.append(s1_max)

    for i in range(1, len(nums) - k + 1):
        res.append(i)

    print(s1)
    # return res

    # return ans


a = [3, -1, 1, -4]

print(sliding_window_maximum(a, 3))
