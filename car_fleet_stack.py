from collections import deque


def carFleet(positions, speeds, target):
    position_speed = list(zip(positions, speeds))
    position_speed.sort(key=lambda x: x[0])
    reach_times = []
    for i in range(len(position_speed)):
        reach_time = (target - position_speed[i][0]) / position_speed[i][1]
        reach_times.append(reach_time)
    stack = deque()
    for i in range(len(position_speed) - 1, -1, -1):
        if not stack:
            stack.append(
                {
                    "cars": [i],
                    "speed": position_speed[i][1],
                    "position": position_speed[i][0],
                }
            )

        else:
            top_speed = stack[-1]["speed"]
            top_reach_time = (target - stack[-1]["position"]) / top_speed
            if position_speed[i][1] > top_speed and reach_times[i] <= top_reach_time:
                top_element = stack.pop()
                top_element["cars"].append(i)
                stack.append(top_element)
            else:
                stack.append(
                    {
                        "cars": [i],
                        "speed": position_speed[i][1],
                        "position": position_speed[i][0],
                    }
                )
    return len(stack)


print(carFleet([6, 2, 17], [3, 9, 2], 20))
