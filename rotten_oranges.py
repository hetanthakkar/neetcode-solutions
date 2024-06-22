from collections import deque


class Graph:
    def __init__(self, matrix):

        self.nodes = 0
        self.top = 0
        self.matrix = matrix.copy()
        for row in matrix:
            self.nodes += len(row)
        self.level = [-1 for _ in range(self.nodes)]
        self.adj_list = [[] for _ in range(self.nodes)]
        self.top = len(matrix[0])
        rotten_oranges = sum(1 for row in self.matrix for cell in row if cell == 2)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self._connect_neighbors(i, j, rotten_oranges)

    def _connect_neighbors(self, i, j, rotten_oranges):
        top = bottom = right = left = None
        current = self.matrix[i][j]
        if 0 <= i < len(self.matrix):
            if 0 <= j - 1 < len(self.matrix[0]):
                left = self.matrix[i][j - 1]
        if 0 <= i < len(self.matrix):
            if 0 <= j + 1 < len(self.matrix[0]):
                right = self.matrix[i][j + 1]
        if 0 <= i - 1 < len(self.matrix):
            if 0 <= j < len(self.matrix[0]):
                top = self.matrix[i - 1][j]
        if 0 <= i + 1 < len(self.matrix):
            if 0 <= j < len(self.matrix[0]):
                bottom = self.matrix[i + 1][j]

        if current in {1, 2}:
            if rotten_oranges > 0 and top is not None and top != 0:
                self.adj_list[(i - 1) * len(self.matrix[i - 1]) + j].append(
                    i * len(self.matrix[i]) + j
                )
                self.adj_list[i * len(self.matrix[i]) + j].append(
                    (i - 1) * len(self.matrix[i - 1]) + j
                )
            if rotten_oranges > 0 and bottom is not None and bottom != 0:
                self.adj_list[(i + 1) * len(self.matrix[i + 1]) + j].append(
                    i * len(self.matrix[i]) + j
                )
                self.adj_list[i * len(self.matrix[i]) + j].append(
                    (i + 1) * len(self.matrix[i + 1]) + j
                )
            if rotten_oranges > 0 and left is not None and left != 0:
                self.adj_list[(i) * len(self.matrix[i]) + j - 1].append(
                    i * len(self.matrix[i]) + j
                )
                self.adj_list[i * len(self.matrix[i]) + j].append(
                    (i) * len(self.matrix[i]) + j - 1
                )
            if rotten_oranges > 0 and right is not None and right != 0:
                self.adj_list[(i) * len(self.matrix[i]) + j + 1].append(
                    i * len(self.matrix[i]) + j
                )
                self.adj_list[i * len(self.matrix[i]) + j].append(
                    (i) * len(self.matrix[i]) + j + 1
                )

    def bfs(self, src):
        bfs = []
        q = deque()
        self.level[src - 1] = 0
        first_connected_nodes = self.adj_list[src - 1]
        for node in first_connected_nodes:
            self.level[node] = self.level[src - 1] + 1
            self.matrix[node // self.top][node % self.top] = 2
            q.appendleft(node)

        processed = set()
        bfs.append(src)
        while q:
            removed = q.pop()
            processed.add(removed)
            if removed + 1 not in bfs:
                bfs.append(removed + 1)
            connected = self.adj_list[removed]
            if isinstance(connected, list):
                for node in connected:
                    if node not in q and node not in processed and node != src - 1:
                        processed.add(node)
                        q.appendleft(node)
                        self.matrix[node // self.top][node % self.top] = 2
                        self.level[node] = self.level[removed] + 1

        return bfs

    def multi_source(self, src):
        self.level.append(-1)
        self.adj_list.append([i - 1 for i in src])
        self.bfs(len(self.adj_list))

    def find_rotten_oranges(self):
        temp = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 2:
                    temp.append(i * len(self.matrix[i]) + j + 1)

        self.multi_source(temp)
        rotten_oranges = 0
        fresh_oranges = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if rotten_oranges != 0 and self.matrix[i][j] == 1:
                    return -1
                if self.matrix[i][j] == 2:
                    rotten_oranges += 1
                if self.matrix[i][j] == 1:
                    fresh_oranges += 1

        if fresh_oranges > 0 and rotten_oranges >= 0:
            return -1
        if max(self.level) == 0:
            return 0

        return max(self.level) - 1


class Solution:
    def orangesRotting(self, grid):
        g1 = Graph(grid)
        return g1.find_rotten_oranges()
