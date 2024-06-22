from collections import deque


def daily_temperatures(temperatures):
    stack = deque()
    res = []
    for i in range(len(temperatures) - 1, -1, -1):
        if len(stack) == 0:
            res.append(-1)
            stack.append(i)
        else:
            top = temperatures[stack[-1]]
            if temperatures[i] >= top:
                while stack and top <= temperatures[i]:
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

    final = []
    res = list(reversed(res))

    for j in range(0, len(res)):
        if res[j] == -1:
            final.append(0)
        else:
            final.append(res[j] - j)

    return final


a = [3, 3, 4]

print(daily_temperatures(a))
