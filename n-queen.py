def solve(n):
    sol = []
    init_row = 0
    current = 0
    band = set()
    queen_position = []

    def check_queen_attack(row, col):
        banned_pos = [tuple([row, col])]
        banned_rows = []
        banned_cols = []
        left_positions = []
        right_positions = []
        banned_diagonals = []
        j = col
        i = row
        while True:
            i += 1
            j -= 1
            if j < 0 or i > n - 1 or j > n - 1:
                break
            left_positions.append(tuple([i, j]))
        j = col
        i = row
        while True:
            i += 1
            j += 1
            if i > n - 1 or j > n - 1:
                break
            right_positions.append(tuple([i, j]))
        banned_diagonals = left_positions + right_positions
        j = col
        i = row
        for k in range(n):
            banned_rows.append(tuple([k, col]))
        j = col
        i = row
        for k in range(n):
            banned_rows.append(tuple([row, k]))
        banned_pos += banned_cols + banned_rows + banned_diagonals
        return banned_pos

    def get_candidates(init_row):

        pos = []

        for row in range(init_row, n):
            for col in range(0, n):
                if (row, col) not in band:
                    pos.append(tuple([row, col]))
        return pos

    def search(state):
        nonlocal current
        nonlocal sol
        nonlocal init_row
        nonlocal band

        if len(queen_position) == n:
            sol.append(queen_position.copy())
            return

        for candidate in get_candidates(init_row):
            queen_position.append(tuple([candidate[0], candidate[1]]))
            temp = check_queen_attack(candidate[0], candidate[1])
            orignal_band = band.copy()
            band.update(temp)
            current += 1
            init_row = candidate[0]
            search(state)
            band = orignal_band
            queen_position.pop()
            current -= 1

        return sol

    temp = search(current)
    print(temp)
    ans = []
    for s in temp:
        board = [["." for _ in range(n)] for _ in range(n)]
        for pos in s:
            board[pos[0]][pos[1]] = "Q"
        ans.append(["".join(row) for row in board])
    return ans


print(solve(9))
