from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


# left always grandparent karta larger


def validate_bst(root, temp, seen):
    if root:
        if root.val in seen:
            temp = 1
            return "False"
        seen.add(root.val)
        if root.left:
            res = validate_bst(root.left, temp, seen)
            if res == "False":
                return "False"
        temp.append(root.val)
        if root.right:
            res = validate_bst(root.right, temp, seen)
            if res == "False":
                return "False"


class Solution:
    def levelOrder(self, root):
        temp = []
        seen = set()
        ret = validate_bst(root, temp, seen)
        if ret == "False":
            return False
        if temp[::-1] == temp and len(temp) > 1:
            return False
        if sorted(temp) == temp:
            return True
        return False


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(2)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(6)
# root = TreeNode(34)
# root.left = TreeNode(-6)
# root.left.left = TreeNode(-21)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

sol = Solution()
print(sol.levelOrder(root))
