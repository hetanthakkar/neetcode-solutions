def maxCoins(nums):
    memo = {}

    def search(state):
        state_key = tuple(state)
        if state_key in memo:
            return memo[state_key]
        if len(state) == 1:
            return state[0]

        current_max = float("-inf")
        for j in range(len(state)):
            prev = state[j - 1] if j - 1 >= 0 else 1
            next = state[j + 1] if j + 1 < len(state) else 1
            current = state[j]

            remaining_state = state[:j] + state[j + 1 :]
            coins = prev * current * next + search(remaining_state)
            current_max = max(current_max, coins)

        memo[state_key] = current_max
        return current_max

    return search(nums)


print(maxCoins([8, 3, 4, 3, 5, 0, 5, 6, 6, 2, 8, 5, 6, 2, 3, 8, 3, 5, 1, 0, 2, 9]))
