# from collections import defaultdict
# def findTargetSum(i,currSum,nums,memo):
#     key = (i,currSum)
#     if key in memo:
#         return memo[key]
    
#     else:
#         if i==len(nums)-1 and (currSum+nums[i]==0 or nums[i]-currSum==0) and nums[i]==0:
#             return 2
#         if i==len(nums)-1 and (currSum+nums[i]==0 or nums[i]-currSum==0):
#             return 1
        
#         if i==len(nums)-1 and currSum+nums[i]!=0:
#             return 0

#         x=findTargetSum(i+1,currSum-nums[i],nums,memo)
#         y=findTargetSum(i+1,currSum+nums[i],nums,memo)
    
#     return x+y

# def findTargetSum1(target,nums):
#     memo=defaultdict(float)
#     return findTargetSum(0,target,nums,memo)

# print(findTargetSum1(1,[1,0]))


def findTargetSum(i,currSum,nums,dp):
    if i==len(nums)-1 and (currSum+nums[i]==0 or nums[i]-currSum==0) and nums[i]==0:
        return 2
    if i==len(nums)-1 and (currSum+nums[i]==0 or nums[i]-currSum==0):
        return 1
    
    if i==len(nums)-1 and currSum+nums[i]!=0:
        return 0
    
    if dp[i][currSum]!=0:
         return dp[i][currSum]
    else:
        x=findTargetSum(i+1,currSum-nums[i],nums,dp)
        y=findTargetSum(i+1,currSum+nums[i],nums,dp)
        dp[i][currSum]= x+y
        return x+y



def findTargetSumWays(nums, target):
        dp = [[0 for _ in range(2*sum(nums)+1)] for _ in range(len(nums)+1)]
        return findTargetSum(0,target,nums,dp)

print(findTargetSumWays([9,7,0,3,9,8,6,5,7,6],2))



# -1 +1 +1 +1 +1
# -1 +1 -1 +1 +1
# -1 -1 +1
# -1 -1 -1
# 2
# [1,1]
# [+1,+1]
# [-1,+1]