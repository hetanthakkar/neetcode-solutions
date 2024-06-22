def solve(nums):
    solutions = []
    state = []

    def search(i):
        if i == len(nums):
            solutions.append(state.copy())
            return
        if i == len(nums) + 1:
            return
        search(i + 1)
        state.append(nums[i])
        search(i + 1)
        state.pop()

    search(0)
    return solutions


print(solve([1, 2, 3]))
