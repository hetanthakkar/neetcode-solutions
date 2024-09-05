from collections import deque, defaultdict


#  we want to maintain left max level and right max level at each node.
# then we can use dfs or bfs to visit that node and find the max
class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


def constructTree(preorder, inorder, seen, index_map):
    if inorder == []:
        return None
    if len(inorder) == 1:
        seen.add(preorder.index(inorder[0]))
        return TreeNode(inorder[0])
    y = None
    for i in range(len(preorder)):
        if i not in seen:
            y = i
            break
    if y == None:
        return None
    seen.add(y)
    root = TreeNode(preorder[y])
    x = None
    if preorder[y] in index_map:
        x = index_map[preorder[y]]
    org_seen = seen
    root.left = constructTree(preorder, inorder[:x], seen, index_map)
    if root.left == None:
        seen = org_seen
    if x == None:
        return None
    else:
        root.right = constructTree(preorder, inorder[x + 1 :], seen, index_map)
    return root


class Solution:
    def buildTree(self, preorder, inorder):
        seen = set()
        index_map = {}
        for i, item in enumerate(preorder):
            index_map[item] = i
        a = constructTree(preorder, inorder, seen, index_map)
        print("asdklfn")


# root = TreeNode(3)
# root.left = TreeNode(3)
# root.right = TreeNode(4)
# root.left.left = TreeNode(4)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

sol = Solution()
print(sol.buildTree([1, 2, 3], [1, 2, 3]))
# print(sol.buildTree([1, 2], [1, 2]))
