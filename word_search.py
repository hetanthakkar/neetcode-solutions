def solve(board, word):
    solutions = False
    height = len(board)
    width = len(board[0])
    seen = set()
    state = []

    def get_candidates(i, j, seen):
        neighbor = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                if tuple([ni, nj]) not in seen:
                    neighbor.append(tuple([ni, nj]))

        return neighbor

    def search(i, j, current):
        nonlocal solutions

        if len(state) == len(word):
            solutions = True
            return
        for candidate in get_candidates(i, j, seen):
            if current > len(word) - 1:
                return
            if board[candidate[0]][candidate[1]] == word[current]:
                state.append(word[current])
                seen.add((candidate[0], candidate[1]))
                search(candidate[0], candidate[1], current + 1)
                seen.remove((candidate[0], candidate[1]))
                state.pop()
                if solutions:
                    return

    for row in range(height):
        for col in range(width):
            if board[row][col] == word[0]:
                if len(word) == 1:
                    return True
                state.append(word[0])
                seen.add((row, col))
                search(row, col, 1)
                if solutions:
                    return True
                seen.clear()
                state = []

    return solutions


board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
print(solve(board, word))
