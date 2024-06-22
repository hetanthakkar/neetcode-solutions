from collections import deque


def get_smaller(temperatures, direction="left"):
    stack = deque()
    res = []

    if direction == "left":
        range_start, range_end, step = 0, len(temperatures), 1
    else:
        range_start, range_end, step = len(temperatures) - 1, -1, -1

    for i in range(range_start, range_end, step):
        if len(stack) == 0:
            res.append(-1)
            stack.append(i)
        else:
            top = temperatures[stack[-1]]
            if temperatures[i] <= top:
                while stack and top >= temperatures[i]:
                    stack.pop()
                    if stack:
                        top = temperatures[stack[-1]]
                if stack:
                    res.append(stack[-1])
                else:
                    res.append(-1)
                stack.append(i)
            else:
                res.append(stack[-1])
                stack.append(i)

    if direction == "right":
        res.reverse()

    return res


def largest_rectangle_histogram(heights):
    left_smaller = get_smaller(heights, "left")
    right_smaller = get_smaller(heights, "right")
    res = []
    back = forward = 0
    for i in range(0, len(heights)):

        back = i - left_smaller[i] - 1

        forward = right_smaller[i] - i - 1
        if back < 0:
            back = 0
        if forward < 0:
            forward = len(heights) - i - 1
        area = heights[i] * (back + forward + 1)
        res.append(area)
    return max(res)


# print(get_left_smaller([0, -1, 1, 2]))
print(largest_rectangle_histogram([1, 1]))
# print(get_global_min([2, -1, 0, 2]))
