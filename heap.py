def heapify(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        
        max_index = i

        while i < n // 2:
            fix = False
            left_index = 2 * i + 1
            right_index = 2 * i + 2

            if left_index < n and arr[left_index] > arr[max_index]:
                max_index = left_index

            if right_index < n and arr[right_index] > arr[max_index]:
                max_index = right_index
                continue

            if arr[max_index] != arr[i]:
                arr[max_index], arr[i] = arr[i], arr[max_index]
                i = max_index
                continue
            i=i*2+1
    return arr


def Klarge(k,arr):
    # count=None
    for _ in range(0,k):
        heapify(arr)
        # if len(arr)>0:
        #     count=arr.pop(0)
    return arr[2]

    def __init__(self, k, nums):
        self.heap=nums
        self.k=k
        

    def add(self, val):

        self.heap.append(val)
        self.heapify(self.heap)
        return self.Klarge(self.k,self.heap)
arr=[4,5,8,2,3,5,10]
print(Klarge(3,arr))
# print(heapify([5,5,2,3]))



  