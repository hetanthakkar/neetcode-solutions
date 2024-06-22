import sys
sys.setrecursionlimit(10000)
def Longest_increasing_subsequence1(i,currentL,nums,dp):
    
    if i>=len(nums)-1 and nums[i]>nums[currentL]:
        return 1
    
    if i>=len(nums)-1 and nums[i]<=nums[currentL]:
        return 0
    
    include=-1

    if dp[i][currentL]!=None:
        return dp[i][currentL]
    else:
        temp=nums[currentL]
        if currentL==-1:
            temp=float('-inf')
        if nums[i]>temp:
            include=Longest_increasing_subsequence1(i+1,i,nums,dp)+1
            
        not_include=Longest_increasing_subsequence1(i+1,currentL,nums,dp)
        dp[i][currentL]=max(include,not_include)
   
        return dp[i][currentL]


def lengthOfLIS(nums):
    dp = [[None for _ in range(len(nums)+ 1)] for _ in range(len(nums) + 1)]
    return Longest_increasing_subsequence1(0, -1,nums, dp)


print(lengthOfLIS([-2,-1]))    



