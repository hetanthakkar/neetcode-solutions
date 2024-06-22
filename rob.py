def rob(i,house,dp):
    
    if i>=len(house):
        return 0
    if i==len(house)-1:
        return house[len(house)-1]
    if dp[i]!=-1:
        return dp[i]
    else:
        c1=rob(i+2,house,dp)+house[i]
        c2=rob(i+1,house,dp)    
        dp[i]= max(c1,c2)
        return dp[i]

def mainRob(nums):
    nums1=nums.copy()
    nums2=nums.copy()
    nums1.pop()
    nums2.pop(0)
    dp=[-1]*(len(nums)+1)
    dp2=[-1]*(len(nums)+1)
    t1=rob(0,nums1,dp)
    t2=rob(0,nums2,dp2)
    print(t1,t2)
    return max(t1,t2)


# def robs(i,house,dp):
#     if i>=len(house):
#         return 0
#     if i==len(house)-1:
#         return house[len(house)-1]
#     if dp[i]!=-1:
#         return dp[i]
#     else:
#         c1=robs(i+2,house,dp)+house[i]
#         c2=robs(i+1,house,dp)    
#         dp[i]= max(c1,c2)
#         return dp[i]


# def rob(nums):
#     dp=[-1]*(len(nums)+1)
#     return robs(0,nums,dp)

print(mainRob([1])) 