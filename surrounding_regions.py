from collections import deque


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.seen = [False for _ in range((self.height * self.width) + 1)]
        self.adj_list = [set() for _ in range(self.height * self.width)]

        for i in range(self.height):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "O":
                    self._connect_neighbors(i, j)

    def _connect_neighbors(self, i, j):
        index = i * len(self.matrix[i]) + j
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < self.height
                and 0 <= nj < self.width
                and self.matrix[ni][nj] == "O"
            ):
                neighbor_index = ni * len(self.matrix[ni]) + nj
                if neighbor_index not in self.adj_list[index]:
                    self.adj_list[index].add(neighbor_index)
                    self.adj_list[neighbor_index].add(index)

    def check_border(self, i, j):
        return i == 0 or j == 0 or i == self.height - 1 or j == self.width - 1

    def dfs(self, src):
        dfs = set([src])
        stack = deque([src - 1])
        if self.seen[src]:
            return dfs

        while stack:
            removed = stack.pop()
            if (
                self.seen[removed] == True
                or self.check_border(removed // self.width, removed % self.width)
                == True
            ):
                return []

            self.seen[removed] = True
            if removed + 1 not in dfs:
                dfs.add(removed + 1)
            connected = self.adj_list[removed]
            for node in connected:
                if node not in stack and node + 1 not in dfs:
                    stack.append(node)

        return list(dfs)

    def get_surrounded_regions(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                current_element = i * len(self.matrix[i]) + j + 1
                if (
                    not self.seen[current_element]
                    and self.matrix[i][j] == "O"
                    and not self.check_border(i, j)
                ):
                    result = self.dfs(current_element)
                    for element in result:
                        self.matrix[element // self.width][
                            element % self.width - 1
                        ] = "X"
        return self.matrix


board = [
    ["X", "X", "X", "X", "X"],
    ["X", "O", "O", "O", "X"],
    ["X", "X", "O", "O", "X"],
    ["X", "X", "X", "O", "X"],
    ["X", "O", "X", "X", "X"],
]


class Solution:
    def solve(self, grid):
        g1 = Graph(grid)
        print("hey")
        return g1.get_surrounded_regions()


print(Solution().solve(board))
