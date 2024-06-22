import math
count=0

def merge(arr1, arr2):
    global count
    left = arr1.copy() + [9999]
    right = arr2.copy()+[9999]
    x=arr1.copy()
    y=arr2.copy()
    new_right=[]
    for i in y:
        new_right.append(i*2)
    newArr = []
    leftPointer = rightPointer = 0
    for i in range(len(left)+len(right)):
            if(leftPointer<=len(x)-1 and rightPointer<=len(new_right)-1 and x[leftPointer]>new_right[rightPointer]):

                count=count+((len(x))-leftPointer)
                print("hey",new_right[rightPointer]*2)
                # count=count+1
                rightPointer += 1
                leftPointer=0
            else:
                leftPointer+=1
        # else:
        #     if (leftPointer<=len(left)-1 and left[leftPointer] != 9999):
        #         leftPointer += 1
    leftPointer = rightPointer = 0
    for i in range(len(left)+len(right)):
        if left[leftPointer] > right[rightPointer]:

            if (  right[rightPointer] != 9999):
                newArr.append(right[rightPointer])
                rightPointer += 1
        else:
            if (left[leftPointer] != 9999):
                newArr.append(left[leftPointer])
                leftPointer += 1
    # print(count)
    return newArr

def mergeSort(array):

    if (len(array) == 1):
        return array
    leftArray = array[:int(len(array)/2)]
    rightArray = array[int(len(array)/2):]
    arr1 = mergeSort(leftArray)
    arr2 = mergeSort(rightArray)
    sortedArray = merge(arr1, arr2)
    # print(count)
    return sortedArray



mergeSort([2,4,3,5,1])
print(count)
