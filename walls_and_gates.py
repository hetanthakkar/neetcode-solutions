# construct a graph such that there is an edge between empty space and empty space and gate.
# do bfs from all the gates and record the time it takes to reach every empty space
# take min of all the bfs result at all empty space

from collections import deque


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.level = [-1 for _ in range((self.height * self.width) + 1)]
        self.seen = [False for _ in range((self.height * self.width) + 2)]
        self.adj_list = [set() for _ in range(self.height * self.width)]
        self.sources = []
        for i in range(self.height):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] != -1:
                    self._connect_neighbors(i, j)
                if self.matrix[i][j] == 0:
                    self.sources.append(i * len(self.matrix[i]) + j + 1)

    def _connect_neighbors(self, i, j):
        index = i * len(self.matrix[i]) + j
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < self.height
                and 0 <= nj < self.width
                and self.matrix[ni][nj] != -1
            ):
                neighbor_index = ni * len(self.matrix[ni]) + nj
                if neighbor_index not in self.adj_list[index]:
                    self.adj_list[index].add(neighbor_index)
                    self.adj_list[neighbor_index].add(index)

    def bfs(self, src):
        bfs = set([src])
        self.level[src - 1] = 0
        queue = deque([src - 1])
        if self.seen[src]:
            return bfs
        while queue:
            removed = queue.pop()
            self.seen[removed] = True
            bfs.add(removed + 1)
            connected = self.adj_list[removed]
            for node in connected:
                if node not in queue and node + 1 not in bfs:
                    queue.appendleft(node)
                    self.level[node] = self.level[removed] + 1

        return list(bfs)

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

    def multi_source(self, src):
        self.level.append(-1)
        self.adj_list.append([i - 1 for i in src])
        self.bfs(len(self.adj_list))
        return self.level

    def assign_distance(self):
        levels = self.multi_source(self.sources)
        for i in range(0, len(levels) - 2):
            print(levels[i], "hey")
            if self.matrix[i // self.width][i % self.width] == -1:
                self.matrix[i // self.width][i % self.width] = -1
                continue
            if self.matrix[i // self.width][i % self.width] == 0:
                self.matrix[i // self.width][i % self.width] = 0
                continue
            else:
                if levels[i] - 1 < 0:
                    self.matrix[i // self.width][i % self.width] = 2147483647
                else:
                    self.matrix[i // self.width][i % self.width] = levels[i] - 1

        return self.matrix


class Solution:
    def wallsAndGates(self, rooms):
        g1 = Graph(rooms)
        return g1.assign_distance()


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

# rooms = [[-1]]
# rooms = [[2147483647]]
print(Solution().wallsAndGates(rooms))
