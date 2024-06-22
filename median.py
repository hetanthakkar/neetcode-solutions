import heapq

class MedianFinder:
    

    def __init__(self):
        self.nums, self.max_heap, self.min_heap = [], [], []
        self.median=None

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        if len(self.nums) == 1:
            self.median=num
            return
        if len(self.nums) == 2:
            if self.nums[0] == max(self.nums[0], self.nums[1]):
                self.min_heap.append(self.nums[0])
                self.max_heap.append(-1*self.nums[1])
            else:
                self.max_heap.append(-1*self.nums[0])
                self.min_heap.append(self.nums[1])
            return

        if num >= self.median:
            heapq.heappush(self.min_heap, num)

        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.min_heap)-len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap)-len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    

    def findMedian(self) -> float:
        if len(self.nums) == 1:
            self.median=self.nums[0]
            return self.median
        if len(self.nums) == 2:
            self.median= (self.nums[0] + self.nums[1]) / 2
            return self.median

        if len(self.nums) % 2 == 0:
            self.median=(self.min_heap[0] + (-1 * self.max_heap[0])) / 2
            return self.median
        else:
            if len(self.min_heap) > len(self.max_heap):
                self.median= self.min_heap[0]
            else:
                self.median= -1 * self.max_heap[0]
            return self.median



mf = MedianFinder()


mf.addNum(1)
print(mf.findMedian())

mf.addNum(2)
print(mf.findMedian())

mf.addNum(3)
print(mf.findMedian())

mf.addNum(4)
print(mf.findMedian())

mf.addNum(5)
print(mf.findMedian())
