import math


def mergeSort(A,p,q):
    r=math.floor((p+q)/2)
    if(p!=r):
        mergeSort(A,p,r)
        mergeSort(A,r,q)
    merge(A,p,q,r)
    return A

def merge(A,p,q,r):
    left=p
    right=r+1
    left_arr=A[p:r+1]
    right_arr=A[r+1:q]

    print(left_arr,right_arr)
    # print(A[left],A[right])
    # while(left<=r or right<=q):
    #     if(A[left]<A[right]):
    #         A[p]=A[left]
    #         left=left+1
    #     else:
    #         A[p]=A[right]
    #         right=right+1
    
    # while(left<=mid or right<=q):
    #     if(A[left]<A[right]):
    #         A[p]=A[left]
    #         left=left+1
    #     else:
    #         A[q]=A[right]
    #         right=right+1

mergeSort([2,1],0,1)
        