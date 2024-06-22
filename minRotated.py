import math


def binary_search(i,j,nums,target):
    if j<i:
        mid=(math.floor(((j+len(nums))+i)/2))%len(nums)
    else:
        mid=math.floor((i+j)/2)

    mid_element=nums[mid]
    if mid_element==target:
        return mid
    if j-i==1 or i-j==len(nums)-1:
        if(j>len(nums)-1):
            j=j%len(nums)
        if nums[i]==target:
            return i
        if nums[j]==target:
            return j
        return -1
    else:
        if target<mid_element:
            j=mid
            # j=i+(len(nums)-mid)
            return binary_search(i,j,nums,target)
        else:
            i=mid
            
            return binary_search(i,j,nums,target)
def ab(i,j, nums):
    first=nums[i]
    if j<i:
        mid=math.floor(((j+len(nums))+i)/2)
    else:
        mid=math.floor((i+j)/2)
    mid_element=nums[mid]
    
    if j-i==1 or i-j==len(nums)-1:
        if(j>len(nums)-1):
            j=j%len(nums)
        if(j>len(nums)-1):
            j=j%len(nums)
        if min(nums[i] ,nums[j])==nums[i]:
            return i
        else:
            return j
    else:
        if first<mid_element:
            i=mid
            j=i+(len(nums)-mid)
            return ab(i,j,nums)
        else:
            j=mid
            return ab(i,j,nums)
             
def search(nums,target):
    starting_index=ab(0,len(nums)-1,nums)
    if starting_index==0:
        ending_index=len(nums)-1
    else:
        ending_index=starting_index-1
    return binary_search(starting_index,ending_index,nums,target)

nums=[1,3,5]
target=1
print(search(nums,target))
print(ab(0,len(nums)-1,nums))

# 1 2 3 4 5 6 7