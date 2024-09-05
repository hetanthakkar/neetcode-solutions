import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.heap = nums[:]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        self.k = k

    def add(self, val):
        min = self.heap[0] if self.heap else float("-inf")
        if val >= min:
            heapq.heappush(self.heap, val)
            while len(self.heap) > self.k:
                heapq.heappop(self.heap)
        return self.heap[0]


k_large = KthLargest(2, [0])
print(k_large.add(-1))
# print(k_large.add(5))
# 2 4 5 8 10 12
# 1 2 3 4  5 6
