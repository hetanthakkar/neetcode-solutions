def product_except_self(nums):
    left_prefix = []
    right_prefix = []
    temp = 1
    temp1 = 1
    for i in nums:
        temp = temp * i
        left_prefix.append(temp)
    for i in reversed(nums):
        temp1 = temp1 * i
        right_prefix.append(temp1)
    right_prefix.reverse()
    print(left_prefix)
    print(right_prefix)
    res = []
    for i in range(0, len(nums)):
        if i == 0:
            product = left_prefix[1]
        elif i == len(nums) - 1:
            product = left_prefix[-2]
        else:
            a = left_prefix[i - 1]
            b = right_prefix[i + 1]
            product = a * b
        res.append(product)

    return res


print(product_except_self([4, 3, 2, 1, 2]))
