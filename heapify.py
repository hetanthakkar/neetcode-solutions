def heapify(arr,n,j):
    
    while True:
        min_index = n//2-1
        left_index = (2 * min_index + 1) 
        right_index = (2 * min_index + 2)

        if left_index < len(arr) and arr[left_index] > arr[min_index]:
            min_index = left_index

        if right_index < len(arr) and arr[right_index] > arr[min_index]:
            min_index = right_index

        if min_index != n//2-1:
            arr[min_index], arr[j] = arr[j], arr[min_index]
            j = min_index

        else:
            break

    return arr

def heapSort(arr):
    for i in range(0, len(arr)):
        n=len(arr)-i
        heapify(arr,n,i)
    return arr

print(heapSort([5,1,1,2,0,0]))  # [1, 5, 6, 9, 10, 12]


#           5
#         /   \
#        1     1
#       / \   /   
#      2   0 0  


#           5
#         /   \
#        2     1
#       / \   /    
#      1   0 0   




# print(heapSort([5,2,3,1]))  # [1, 5, 6, 9, 10, 12]