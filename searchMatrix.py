import math

def search1(i,j,matrix,target):
    if len(matrix)==1:
        if matrix[i]==target:
            return i
        else:
             return -1
    mid=math.floor((i+j)/2)
    if j-i==1:
        if target<matrix[int(j)] and target<matrix[int(i)]:
            return -1
        return i
    if target>matrix[int(mid)]:
        return search1(mid,j,matrix,target)
    else:
        return search1(i,mid,matrix,target)

def calculate_time(index,nums,temp):
    sum=0
    for i in range(index+1,len(nums)):
        d=math.floor(temp)
        if d==0:
            d=math.ceil(temp)
        sum=sum+math.ceil(nums[i]/d)
    return sum

def bananas(nums,target,i,j):
    nums.sort()
    temp=(j+i)/2
    if math.floor(temp)==0:
        return 1
    index=search1(0,len(nums)-1,nums,temp)
    sum1=calculate_time(index,nums,temp)
    time=sum1+index+1
    if(j-temp<1):
         if time>target:
             return math.floor(j)
         else:
             return math.floor(temp)
    if (j-i<1):
         return math.floor(i)
    if(time>target):
        return bananas(nums,target,temp,j)
    if(time<=target):
       return bananas(nums,target,i,temp)
# nums = [83, 95, 628, 97]

# target = 100
# nums = [3,6,7,11]

# target = 8
nums = [312884470]

target = 968709470
# nums = [2,2]

# target = 4
print(bananas(nums, target, 0, max(nums))) #11
# print(minEatingSpeed(nums, target)) #10
# 
# 83, 95, 97, 628