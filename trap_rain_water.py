def trap(height):
    area = 0
    leftPointer = 0
    rightPointer = len(height) - 1
    leftMax = 0
    rightMax = 0
    while leftPointer < rightPointer:
        leftMax = max(leftMax, height[leftPointer])
        rightMax = max(rightMax, height[rightPointer])
        if leftMax < rightMax:
            trapped = leftMax - height[leftPointer]
            leftPointer += 1
        else:
            trapped = rightMax - height[rightPointer]
            rightPointer -= 1

        area += trapped
    return area


height = [4, 2, 0, 3, 2, 5]
print(trap(height))
# print(trap([4, 2, 0, 3]))
# print(trap([4, 2, 3]))
