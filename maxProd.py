def maxProduct(i,prod,nums):
    if i==len(nums):
        return nums[i]
    
    if nums[i]>prod*nums[i]:
        return nums[i]
    include=maxProduct(i+1,prod*nums[i],nums)
    not_include=maxProduct(i+1,prod,nums)
    return max(include,not_include)

print(maxProduct(0,0,[2,0,3]))


# keep track of minimum and maximum