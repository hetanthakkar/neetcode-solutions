import math
count=0

class Solution:
    def __init__(self):
        self.count = 0

    def merge(self,arr1, arr2,mx):

        # global count
        left = arr1.copy() + [200000000004]
        right = arr2.copy()+[mx]
        x=arr1.copy()
        y=arr2.copy()
        # new_right=[]
        new_right = [i * 2 for i in y]  # Calculate new_right directly
        # for i in y:
        #     new_right.append(i*2)
        newArr = []
        leftPointer = rightPointer = 0
        while leftPointer < len(x) and rightPointer < len(new_right):
            if(leftPointer<=len(x)-1 and rightPointer<=len(new_right)-1 and x[leftPointer]>2*new_right[rightPointer]):
                self.count=self.count+((len(x))-leftPointer)
                # print("hey",new_right[rightPointer]*2)
                rightPointer += 1
                leftPointer=0
            else:
                leftPointer+=1

        leftPointer = rightPointer = 0
        for i in range(len(left)+len(right)):
            if leftPointer<=len(left)-1 and left[leftPointer] > right[rightPointer]:

                if (right[rightPointer] != mx):
                    newArr.append(right[rightPointer])
                    rightPointer += 1
            else:
                if (left[leftPointer] != mx):
                    newArr.append(left[leftPointer])
                    leftPointer += 1
        # print(count)
        
        return newArr

    def mergeSort(self,array,mx):
        

        if (len(array) == 1):
            return array
        leftArray = array[:int(len(array)/2)]
        rightArray = array[int(len(array)/2):]
        arr1 = self.mergeSort(leftArray,mx)
        arr2 = self.mergeSort(rightArray,mx)
        sortedArray = self.merge(arr1, arr2,mx)
        # print(count)
        return sortedArray


    
    def reversePairs(self, nums):
        
        self.count = 0  
        mx=max(nums)+9999
        # print(mx)
        self.mergeSort(nums,mx)
        return self.count
        



print(Solution().reversePairs([233,234,20003,236,233,233,233]))
# print(Solution1().reversePairs([233,234,20003,236,233,233,233]))
