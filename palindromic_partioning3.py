def partition(s, k):
    state = []
    memo = {}

    def search(current):
        counter = float("inf")
        nonlocal state

        if s == "".join(state) and len(state) == k:
            count = 0
            for st in state:
                for i in range(0, (len(st) + 1) // 2):
                    if st[i] != st[len(st) - i - 1]:
                        count += 1
            counter = min(counter, count)
            memo[current] = counter
            return counter

        for candidate in range(current, len(s)):
            state.append(s[current : candidate + 1])
            counter = min(counter, search(candidate + 1))
            state.pop()

        return counter

    return search(0)


print(partition("abc", 2))
