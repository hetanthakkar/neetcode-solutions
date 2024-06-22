def valid_sudoku(sudoku):

    for row in sudoku:
        seen = set()
        for element in row:
            if element.isdigit():
                if element not in seen:
                    seen.add(element)
                else:
                    return False

    rows = len(sudoku)
    cols = len(sudoku[0])
    for col in range(cols):
        seen1 = set()
        for row in range(rows):
            element = sudoku[row][col]
            if element.isdigit():
                if element not in seen1:
                    seen1.add(element)
                else:
                    return False

    seen = [set() for _ in range(9)]
    for i in range(rows):
        for j in range(0, cols):
            sub_grid_index = (i // 3) * 3 + (j // 3)
            if sudoku[i][j].isdigit():
                if sudoku[i][j] in seen[sub_grid_index]:
                    return False
                else:
                    seen[sub_grid_index].add(sudoku[i][j])

    return True

    # print(element)


values = list(range(1, 82))

# Create the 9x9 matrix
matrix = [values[i : i + 9] for i in range(0, 81, 9)]

# print(matrix)

sudoku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(valid_sudoku(sudoku))
