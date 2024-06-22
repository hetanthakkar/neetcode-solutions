
def min_operations_to_equalize(arr):
    arr.sort()
    median = arr[len(arr) // 2] if len(arr) % 2 == 1 else arr[len(arr) // 2 - 1]

    total_operations = 0
    for num in arr:
        total_operations += abs(num - median) // 2

    return total_operations

def minCycles(i,currDiff,isEven,nums):
    if currDiff==0 or i>=len(nums):
        return 0
    
    else:
        if isEven:
            increment=minCycles(i+2,currDiff+2,False,nums)+1
            do_nothing=minCycles(i+1,currDiff,False,nums)
        if not isEven:
            increment=minCycles(i+1,currDiff+1,True,nums)+1
            do_nothing=minCycles(i+1,currDiff,True,nums)
    
    return max(increment,do_nothing)

nums=[4,4,3,5,5]
minimum=min(nums)
maximum=max(nums)
diff=minimum-maximum
# print(minCycles(0,diff,False,nums))
print(min_operations_to_equalize(nums))


# [1,2]