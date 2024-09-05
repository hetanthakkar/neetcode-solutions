def numRollsToTarget(n,k,target):
    memo={}
    def search(taken,sum):
        if (taken,sum) in memo:
            return memo[(taken,sum)]
        count=0
        if sum==target :
            return 1
        if taken==n:
            return 0
        for i in range(1,k+1):
            count+=search(taken+1,sum+i)
        memo[(taken,sum)]=count % (10**9 + 7)
        return memo[(taken,sum)]
    return search(0,0)

print(numRollsToTarget(30,30,500))