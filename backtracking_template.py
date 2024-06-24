def solve():
    solutions = []
    state = []

    def is_valid_state(state):
        return True

    def get_candidates(state):
        return []

    def search(state):
        if is_valid_state(state):
            solutions.append(state.copy())
            return

        for candidate in get_candidates(state):
            state.append(candidate)
            search(state)
            state.remove(candidate)

        return solutions

    return search(state)
