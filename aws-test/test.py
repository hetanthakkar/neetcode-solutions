def partition(s, k):
    state = []
    counter = float("inf")

    def search(current):
        nonlocal state
        nonlocal counter
        if s == "".join(state) and len(state) == k:
            count = 0
            for st in state:
                for i in range(0, (len(st) + 1) // 2):
                    if st[i] != st[len(st) - i - 1]:
                        count += 1
            counter = min(counter, count)
            return

        for candidate in range(current, len(s)):
            state.append(s[current : candidate + 1])
            search(candidate + 1)
            state.pop()

    search(0)
    return counter


print(partition("abc", 2))
