def combination_sum(candidates, target):

    def search(state, start, solutions, current_sum):
        if current_sum == target:
            solutions.add(tuple(state))
            return
        if current_sum < target:
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                state.append(candidate)
                org_sum = current_sum
                current_sum += candidate
                search(state, i, solutions, current_sum)
                state.pop()
                current_sum = org_sum

    def solve():
        solutions = set()
        state = []
        candidates.sort()
        current_sum = 0
        search(state, 0, solutions, current_sum)
        return [list(sol) for sol in solutions]

    return solve()
