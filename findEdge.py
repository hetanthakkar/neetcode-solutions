from collections import deque


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.level = [-1 for _ in range(0, nodes)]
        self.list = [set() for _ in range(0, nodes)]
        for i in range(len(edges)):
            self.list[edges[i][0] - 1].add(edges[i][1] - 1)
        self.seen = set()
        self.nodes = 0
        # self.top = 0
        self.level = [-1 for _ in range(self.nodes)]

        self.adj_list = [set() for _ in range(self.nodes)]
        self.top = len(edges[0])

    def find_edge(self, src, destination):
        q = deque()
        first_connected_nodes = self.list[src - 1]
        for i in range(0, len(first_connected_nodes)):
            q.appendleft(first_connected_nodes[i])

        while q:
            removed = q.pop()
            if removed == destination - 1:
                return 1
            connected = self.list[removed]
            if isinstance(connected, list):
                for i in range(0, len(connected)):
                    if connected[i] == destination - 1:
                        return 1
                    if connected[i] not in q:
                        q.appendleft(connected[i])
        return 0

    def bfs(self, src):
        bfs = []
        q = deque()
        self.level[src - 1] = 0
        first_connected_nodes = self.list[src - 1]
        for i in range(0, len(first_connected_nodes)):
            self.level[first_connected_nodes[i]] = self.level[src - 1] + 1
            q.appendleft(first_connected_nodes[i])
        processed = set()
        bfs.append(src)
        while q:
            removed = q.pop()
            processed.add(removed)
            if removed + 1 not in bfs:
                bfs.append(removed + 1)
            connected = self.list[removed]
            if isinstance(connected, list):
                for i in range(0, len(connected)):
                    if (
                        connected[i] not in q
                        and connected[i] not in processed
                        and connected[i] != src - 1
                    ):
                        processed.add(connected[i])
                        q.appendleft(connected[i])
                        self.level[connected[i]] = self.level[removed] + 1

        return bfs

    def multi_source(self, src):
        temp = []
        for i in src:
            temp.append(i - 1)
        self.level.append(-1)
        self.list.add(temp)
        self.bfs(len(self.list))

    def max_time_cover(self, src):
        self.multi_source(src)
        return max(self.level) - 1

    def dfs(self, src):
        dfs = [src]
        stack = deque([src])
        while stack:
            removed = stack.pop()
            if removed not in dfs:
                dfs.append(removed)
            connected = self.list[removed - 1]
            for node in connected:
                if node + 1 not in dfs:
                    stack.append(node + 1)
        return dfs

    def check_border(self, i, j):

        return (
            i == 0
            or j == 0
            # or i == self.top
            or i == self.height - 1
            or j == self.width - 1
            # or j == self.bottom
        )


A = 12
# B=[
#   [1, 4],
#   [2, 1],
#   [4, 3],
#   [4, 5],
#   [2, 3],
#   [2, 4],
#   [1, 5],
#   [5, 3],
#   [2, 5],
#   [5, 1],
#   [4, 2],
#   [3, 1],
#   [5, 4],
#   [3, 4],
#   [1, 3],
#   [4, 1],
#   [3, 5],
#   [3, 2],
#   [5, 2],
# ]

# B=[
#   [1,3],
#   [2, 3],
#   [3,5],
#   [3,4],
#   [4,6],
# #   [5, 4],
# #   [5, 6]
# ]

# B=[
#   [1,4],
#   [1, 2],
#   [2,5],
#   [2,1],
#   [2,3],
#   [3,6],
#   [3,2],
#   [4,1],
#   [4,5],
#   [5, 8],
#   [5, 2],
#   [5, 4],
#   [5, 6],
#   [6,9],
#   [6,3],
#   [6,5],
#   [8,5],
#   [8,9],
#   [9,6],
#   [9,8],
# ]


B = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
# src=1
# destination=8

g1 = Graph(A, B)
# print(g1.bfs(1))
print(g1.dfs(1))
# print(g1.level)
# res= g1.find_edge(src,destination)
# print(res)
