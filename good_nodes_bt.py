from collections import deque, defaultdict


#  we want to maintain left max level and right max level at each node.
# then we can use dfs or bfs to visit that node and find the max
class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, maxi, count):

    if root:
        if root.left:
            if root.left.val >= maxi:
                count[0] += 1
                dfs(root.left, root.left.val, count)
            else:
                dfs(root.left, maxi, count)
        if root.right:
            if root.right.val >= maxi:
                count[0] += 1
                dfs(root.right, root.right.val, count)
            else:
                dfs(root.right, maxi, count)


class Solution:
    def levelOrder(self, root):
        count = [1]
        dfs(root, root.val, count)
        return count[0]


root = TreeNode(3)
root.left = TreeNode(3)
# root.right = TreeNode(4)
root.left.left = TreeNode(4)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

sol = Solution()
print(sol.levelOrder(root))
