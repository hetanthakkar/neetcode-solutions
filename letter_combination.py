def solve(digits):
    solutions = []
    state = ""
    current = 0
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", ",n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def get_candidates(current):
        return mapping[digits[current]]

    def is_valid_state(state):

        if len(state) == len(digits):
            return True

    def search(current):
        nonlocal state
        if is_valid_state(state):
            solutions.append(state[:])
            return
        if current > len(digits) - 1:
            return solutions
        for candidate in get_candidates(current):
            state += candidate
            current += 1
            search(current)
            current -= 1
            state = state[:-1]

        return solutions

    return search(current)


digits = "6"
print(solve(digits))
