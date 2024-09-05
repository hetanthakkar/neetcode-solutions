import math
import heapq


def k_closest(points, k):
    heap = []
    index_map = {}
    distance_map = {}
    res = []
    for index, point in enumerate(points):
        distance = math.sqrt(point[0] * point[0] + point[1] * point[1])
        index_map.update({index: distance})
        heapq.heappush(heap, distance)
        if distance in distance_map:
            distance_map[distance].append(index)
        else:
            distance_map[distance] = [index]
    print(index_map)
    print(distance_map)

    for _ in range(k):
        dis = heapq.heappop(heap)
        res.append(points[distance_map[dis][-1]])
        distance_map[dis].pop()
        print(distance_map[dis])
    return res


k_closest([[0, 1], [1, 0]], 2)
