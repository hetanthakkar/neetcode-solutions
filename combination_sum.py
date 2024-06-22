def combination_sum(candidates, target):
    candidates.sort()
    solutions = set()
    state = []
    seen = []

    def get_candidate(i):
        return sorted(list(set(candidates[i:])))

    def search(state, current_sum, start):
        # print(state)

        if current_sum == target:
            solutions.add(tuple(sorted(state[:])))
            return

        if current_sum > target:
            return

        for candidate in get_candidate(start):
            current_sum += candidate
            state.append(candidate)
            if state not in seen:
                seen.append(state[:])
                search(state, current_sum, start + 1)
            state.pop()
            current_sum -= candidate
            start += 1

    def solve():
        search(state, 0, 0)
        return [list(sol) for sol in solutions]

    return solve()


print(combination_sum([3, 3, 5, 1, 1], 8))
