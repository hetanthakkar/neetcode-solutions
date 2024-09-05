from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


class TreeNode1:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def dfs(root, dic):
    if root:
        if root in dic:
            dic[root].add(root)
        else:
            dic[root] = set()
            dic[root].add(root)
        if root.left:
            dic[root].update(dfs(root.left, dic))
        if root.right:
            dic[root].update(dfs(root.right, dic))
        return dic[root]


class Solution:
    def isSubtree(self, root, p, q):
        dic = {}
        dfs(root, dic)
        node = None
        # print(dic)
        for key, val in dic.items():
            if p in val and q in val:
                node = key
        return node


# root.left = TreeNode(1)
# root = TreeNode(6)
# root.left = TreeNode(2)
# root.right = TreeNode(8)
# root.right.left = TreeNode(7)
# root.right.right = TreeNode(9)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
sroot = TreeNode(3)
sroot.left = TreeNode(1)
sroot.right = TreeNode(4)
sroot.right.left = TreeNode(2)
s = Solution()
print(s.isSubtree(sroot, sroot.right.left, sroot))

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(3)

# sol = Solution()
# print(sol.diameterOfBinaryTree(root))
