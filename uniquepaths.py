def calculate_path(i, j):
    # If we reach the starting point, there's one unique path (not zero)
    if i == 0 and j == 0:
        return 1
    # If we are at the first row, there's only one way to reach here (all horizontal moves)
    if i == 0:
        return calculate_path(i, j - 1)
    # If we are at the first column, there's only one way to reach here (all vertical moves)
    if j == 0:
        return calculate_path(i - 1, j)
    # Otherwise, sum the number of ways from the left and above cells
    return calculate_path(i - 1, j) + calculate_path(i, j - 1)


print(calculate_path(3, 2))
