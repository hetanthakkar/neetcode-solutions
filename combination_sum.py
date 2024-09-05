def combination_sum(candidates, target):
    candidates.sort()
    solutions = set()
    state = []

    def search(state, current_sum, start):

        if current_sum == target:

            solutions.add(tuple(sorted(state[:])))
            return

        if current_sum > target or start > len(candidates) - 1:
            return

        state.append(candidates[start])
        current_sum += candidates[start]
        search(state, current_sum, start + 1)
        state.pop()
        current_sum -= candidates[start]
        search(state, current_sum, start + 1)

    def solve():
        search(state, 0, 0)
        return [list(sol) for sol in solutions]

    return solve()


print(combination_sum([10, 1, 2, 7, 6, 1, 5], 8))
