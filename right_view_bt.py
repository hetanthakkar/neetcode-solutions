from collections import deque, defaultdict


#  we want to maintain left max level and right max level at each node.
# then we can use dfs or bfs to visit that node and find the max
class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, level, dic):
    if root:
        dic[root] = level
        dfs(root.left, level + 1, dic)
        dfs(root.right, level + 1, dic)


class Solution:
    def levelOrder(self, root):
        dic = defaultdict(int)
        res = {}
        final = []
        ans = []
        dfs(root, 0, dic)
        for key, val in dic.items():
            if val in res:
                res[val].append(key)
            else:
                res[val] = [key]
        for val in res.values():
            final.append(val)
        a = [[node.val for node in sublist] for sublist in final]
        for nodes in a:
            ans.append(nodes[-1])
        return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(4)

sol = Solution()
print(sol.levelOrder(root))
