from collections import deque, defaultdict


#  we want to maintain left max level and right max level at each node.
# then we can use dfs or bfs to visit that node and find the max
class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


def isMatch(root1, root2, cot=False):
    if root1 == root2:
        return True
    if root1 is None or root2 is None:
        return False
    else:
        if root1.val == root2.val:
            left_match = isMatch(root1.left, root2.left, True)
            right_match = isMatch(root1.right, root2.right, True)
            if left_match and right_match:
                return True

            else:
                if cot:
                    return False
                else:
                    a = isMatch(root1.right, root2)
                    b = isMatch(root1.left, root2)
                    return a or b
        else:
            if cot:
                return False
            else:
                a = isMatch(root1.right, root2)
                b = isMatch(root1.left, root2)
                return a or b


class Solution:
    def isSubtree(self, root, subRoot):
        if isMatch(root, subRoot):
            return True
        if isMatch(root.left, subRoot):
            return True
        if isMatch(root.right, subRoot):
            return True
        return False


# root.left = TreeNode(1)
root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)

sroot = TreeNode(4)
sroot.left = TreeNode(1)
sroot.left.left = TreeNode(6)
sroot.left.right = TreeNode(7)
s = Solution()
print(s.isSubtree(root, sroot))

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(3)

# sol = Solution()
# print(sol.diameterOfBinaryTree(root))
