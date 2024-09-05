from collections import deque, defaultdict


#  we want to maintain left max level and right max level at each node.
# then we can use dfs or bfs to visit that node and find the max
class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


def dfs_recursive(root, left_level, right_level):
    if root.left:
        left_height = 1 + dfs_recursive(root.left, left_level, right_level)
    else:
        left_height = 0
    if root.right:
        right_height = 1 + dfs_recursive(root.right, left_level, right_level)
    else:
        right_height = 0
    left_level[root] = left_height
    right_level[root] = right_height
    return max(left_height, right_height)


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        left_level = defaultdict(int)
        right_level = defaultdict(int)
        res = 0
        count = [0]
        dfs_recursive(root, left_level, right_level)
        for node in left_level.keys():
            res = max(res, left_level[node] + right_level[node])
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.diameterOfBinaryTree(root))
