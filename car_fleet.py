def car_fleet(target, position, speed):

    position_speed = list(zip(position, speed))
    position_speed.sort(key=lambda x: x[0])
    fleets = {}
    added = set()

    for i in range(0, len(position_speed)):
        current_time_to_reach = (target - position_speed[i][0]) / position_speed[i][1]
        for j in range(len(position_speed) - 1, i, -1):
            other_time_to_reach = (target - position_speed[j][0]) / position_speed[j][1]
            if (
                current_time_to_reach <= other_time_to_reach
                and position_speed[i][0] not in added
            ):
                fleets.setdefault(position_speed[j][0], set()).add(position_speed[i][0])
                added.add(position_speed[i][0])

        if position_speed[i][0] not in added:
            fleets[position_speed[i][0]] = set()

    return len(fleets)


print(car_fleet(10, [6, 8], [3, 2]))
