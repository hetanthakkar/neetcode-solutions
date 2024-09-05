from collections import deque, defaultdict


#  we want to maintain left max level and right max level at each node.
# then we can use dfs or bfs to visit that node and find the max
class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


def isSame(root1, root2):
    if root1 and root2:
        if root1.val == root2.val:
            return isSame(root1.left, root2.left) and isSame(root1.right, root2.right)
        else:
            return False
    else:
        return True


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        left_level = defaultdict(int)
        right_level = defaultdict(int)
        dfs_recursive(root, left_level, right_level)
        for node in left_level.keys():
            if abs(left_level[node] - right_level[node]) > 1:
                return False
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(3)

sol = Solution()
print(sol.diameterOfBinaryTree(root))