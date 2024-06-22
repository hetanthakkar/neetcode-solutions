def canCompleteCircuit(gas, cost):
    total_gas = 0
    for g in gas:
        total_gas += g
    total_cost = 0
    for c in cost:
        total_cost += c
    if total_gas < total_cost:
        return -1
    current_index = -1
    current_sum = 0
    to_track = 0
    for i in range(len(gas)):
        current_sum += gas[i] - cost[i]
        if current_sum >= 0 and current_index == -1:
            current_index = i
            if current_sum == to_track and gas[i] != 0:
                return current_index
        if current_sum < 0:
            current_index = -1
            to_track += current_sum
            current_sum = 0
    return current_index


gas = [2, 3, 4]
cost = [3, 4, 3]
print(canCompleteCircuit(gas, cost))
