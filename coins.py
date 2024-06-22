
def minCoins(i,target,coins,dp):
    if target<=0 or len(coins)==0 or i>=len(coins):
        return 0

    
    if target==coins[i]:
        return 1

    if dp[i][target]!=-1:
         return dp[i][target]
    

    include=minCoins(i,target-coins[i],coins,dp)
    not_include=minCoins(i+1,target,coins,dp)
    dp[i][target]=include+not_include
    return dp[i][target]

def callCoins(amount,coins):
    # if amount
    dp = [[-1 for _ in range(amount+ 1)] for _ in range(len(coins) + 1)]
    y=minCoins(0,amount,coins,dp)
    if y==float('inf'):
        return -1
    return y

print(callCoins(0,[7]))
