def partition(s):
    state = []
    solution = []

    def get_candidates(current):
        sub_index = []
        for i in range(current, len(s)):
            sub_index.append(i)
        return sub_index

    def check_palindrome(start, end):
        return s[start : end + 1][::-1] == s[start : end + 1]

    def search(current):

        nonlocal state

        if s == "".join(state):
            solution.append(state[:])
            return

        for candidate in get_candidates(current):
            if check_palindrome(current, candidate):
                state.append(s[current : candidate + 1])
                search(candidate + 1)
                state.pop()

        return solution

    return search(0)


print(partition("aaa"))
