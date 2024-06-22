def jump_game(nums):
    fuel = 0
    for i, num in enumerate(nums):
        if num + i > fuel:
            fuel = num + i
        if fuel == len(nums) - 1:
            return True
        if fuel == 0:
            return False
    return False
    # start = len(nums) - 1
    # current_index = start - 1
    # while start > 0:
    #     while current_index + nums[current_index] < start:
    #         current_index -= 1
    #     start = current_index
    #     current_index = start - 1
    return True


print(jump_game([3, 2, 1, 0, 4]))
# 2 0 9 3
