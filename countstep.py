def countStep(n):
    dp = [-1] * (n + 1)
    if n==0:
        dp[0]=0
        return 0
    if n==1:
        dp[1]=1
        return 1
    if n==2:
        return 2        
    if n>2:
        dp[1]=1
        dp[0]=0
        dp[2]=2

    for i in range (3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]


print(countStep(3))