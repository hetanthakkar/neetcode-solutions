def solve(matrix):
    height = len(matrix)
    width = len(matrix[0])
    seen = set()
    memo = {}

    def get_candidates(i, j, seen):
        neighbor = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width:
                if tuple([ni, nj]) not in seen:
                    neighbor.append(tuple([ni, nj]))

        return neighbor

    def search(i, j, last):
        max_length = 1
        if tuple([i, j, last]) in memo:
            return memo[tuple([i, j, last])]
        for candidate in get_candidates(i, j, seen):
            if matrix[candidate[0]][candidate[1]] > last:
                original_last = last
                last = matrix[candidate[0]][candidate[1]]
                seen.add((candidate[0], candidate[1]))
                temp = search(candidate[0], candidate[1], last)
                max_length = max(max_length, temp + 1)
                seen.remove((candidate[0], candidate[1]))
                last = original_last
        memo[tuple([i, j, last])] = max_length
        return max_length

    maxLength = 0
    for row in range(height):
        for col in range(width):
            seen.add((row, col))
            ans = search(row, col, matrix[row][col])
            maxLength = max(maxLength, ans)
            seen.clear()

    return maxLength


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
print(solve(matrix))
