import heapq


def lastStoneWeight(stones):
    stones = [-i for i in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        first_stone = heapq.heappop(stones)
        second_stone = heapq.heappop(stones)
        if first_stone != second_stone:
            heapq.heappush(stones, -1 * abs(first_stone - second_stone))
    if len(stones):
        return -stones[0]
    else:
        return 0


print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
