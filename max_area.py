def maxArea(heights):
    area = 0
    leftPointer = 0
    rightPointer = len(heights) - 1
    while leftPointer != rightPointer:
        left = heights[leftPointer]
        right = heights[rightPointer]
        minimum = min(left, right)
        area = max(minimum * (rightPointer - leftPointer), area)
        if left == minimum:
            leftPointer += 1
        else:
            rightPointer -= 1
    return area


print(maxArea([1, 1]))
