from collections import deque, defaultdict


#  we want to maintain left max level and right max level at each node.
# then we can use dfs or bfs to visit that node and find the max
class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


# def bfs(root, queue):
#     temp = []
#     temp1 = []
#     if root:
#         queue.appendleft(root)
#     temp1.append(root)
#     while queue:
#         inser = []
#         removed = queue.pop()
#         temp.append(removed)
#         left = right = 0
#         if removed.left:
#             inser.append(removed.left)
#             queue.appendleft(removed.left)
#             left += 1
#         if removed.right:
#             inser.append(removed.right)
#             queue.appendleft(removed.right)
#             right += 1
#         temp1.append(inser)
#     # print(temp)
#     return temp


# if root.left and root.right exist then their level is root.level+1
def dfs(root, level, dic):
    if root:
        dic[root] = level
        dfs(root.left, level + 1, dic)
        dfs(root.right, level + 1, dic)


# "abc":2,"def":2,"xyz":3
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        dic = defaultdict(int)
        res = {}
        result = []
        final = []
        dfs(root, 0, dic)
        for key, val in dic.items():
            if val in res:
                res[val].append(key)
            else:
                res[val] = [key]
        final = list(res.values())
        a = [[node.val for node in sublist] for sublist in final]
        return a


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

sol = Solution()
print(sol.diameterOfBinaryTree(root))
