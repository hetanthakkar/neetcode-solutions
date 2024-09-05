def solve(nums):
    max_coin = float("-inf")
    state = nums[:]

    def search(i, coins):
        nonlocal state
        nonlocal max_coin
        if len(state) == 1:
            coins += state[0]
            max_coin = max(max_coin, coins)
            return coins

        for j in range(i, len(state)):

            # manipulate state
            original_coins = coins
            if j - 1 < 0:
                prev = 1
            else:
                prev = state[j - 1]
            if j + 1 > len(state) - 1:
                next = 1
            else:
                next = state[j + 1]
            current = state[j]
            original = state[:]
            state.pop(j)
            coins = prev * current * next + search(state)

            coins = original_coins
            state = original

        return max_coin

    temp = search(0, 0)
    return temp


print(solve([3, 1, 5, 8]))
print(solve([2, 4, 8, 4, 0, 7, 8, 9, 1, 2, 4, 7, 1, 7, 3, 6]))
