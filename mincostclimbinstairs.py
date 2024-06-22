def calCost(n,cost,dp):


    if n==len(cost)-1:
        return cost[n]
    
    if n==len(cost):
        return 0

    if dp[n]!=-1:
        return dp[n]
    
    else:
        c1=cost[n]+calCost(n+1,cost,dp)
        c2=cost[n]+calCost(n+2,cost,dp)
        dp[n]=min(c1,c2)
        return min(c1,c2)

def minCost(cost):
    n=0
    cost1=cost.copy()
    cost1.remove(cost[0])
    dp1 = [-1] * (len(cost) + 1)
    dp2 = [-1] * (len(cost) + 1)
    print(cost1)
    t1=calCost(n,cost,dp1)
    t2=calCost(n,cost1,dp2)
    return min(t1,t2)

print(minCost([1,100,1,1,1,100,1,1,100,1]))