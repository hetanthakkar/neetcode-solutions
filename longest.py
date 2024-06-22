

def longestConsecutive(nums):
        if nums == []:
                return 0
        if len(nums) == 1:
                return 1
        hset = set(nums)
        
        currmax = 1
        visited=set()
        
        for i in range(0,len(nums)):
                if nums[i] not in visited:
                    print(visited)
                    src = nums[i] +1
                    j=1
                    while src in hset:                         
                            j+=1
                            visited.add(src)
                            src= src + 1
                    currmax = max(j, currmax)
        print(visited)
        return currmax



print(longestConsecutive([1,2,3]))