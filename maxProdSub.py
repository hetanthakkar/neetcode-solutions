temp=set()
def maxProd(i,nums):
    
    
    if i==0:
        return nums[i]
    
    included=maxProd(i-1,nums)*nums[i]
    excluded=maxProd(i-1,nums)
    t=max(included,excluded)
    
    if t==included:
        temp.add(nums[i])   
        
    return t

print(maxProd(1,[-1,2,-1]))
print(temp)