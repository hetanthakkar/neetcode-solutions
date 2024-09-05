import heapq


def k_closest(nums, k):
    heap = []
    heapq.heapify(nums)
    while len(heap) > k:
        heapq.heappop(heap)
    return heap[0]


k_closest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
