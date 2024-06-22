def jump(self, nums: List[int]) -> int:
    count = 0
    initial_fuel = nums[0]
    if len(nums) == 1:
        return 0
    fuel = 0
    for i, num in enumerate(nums):
        if i > initial_fuel:
            count += 1
            initial_fuel = fuel
        if i == len(nums) - 1:
            return count + 1
        if num + i > fuel:
            fuel = num + i
    return count
