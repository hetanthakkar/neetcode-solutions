from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None, left_level=0, right_level=0):
        self.val = val
        self.left = left
        self.right = right


def dfs_recursive(root, left_level, right_level):
    if root.left:
        left_height = root.val + dfs_recursive(root.left, left_level, right_level)
    else:
        left_height = root.val
    if root.right:
        right_height = root.val + dfs_recursive(root.right, left_level, right_level)
    else:
        right_height = root.val
    left_level[root] = left_height
    right_level[root] = right_height
    return max(left_height, right_height, root.val)


class Solution:
    def buildTree(self, root):
        left_level = defaultdict(int)
        right_level = defaultdict(int)
        res = float("-inf")
        dfs_recursive(root, left_level, right_level)
        for node in left_level.keys():
            res = max(
                res,
                node.val,
                left_level[node],
                right_level[node],
                left_level[node] + right_level[node] - node.val,
            )
        return res


ab = []


def get_string(root, string):
    if root:
        stri = string + "=" + str(root.val)
        ab.append(stri)
        if root.left:
            get_string(root.left, string + "." + "left")
        if root.right:
            get_string(root.right, string + "." + "right")
    final = ""
    for i in ab:
        final = final + i + "hetan"
    return final


def create_tree(address, value, root):
    pointer = root
    address = address[1:]
    last = address.pop()
    for step in address:
        if step == "left":
            pointer = pointer.left
        else:
            pointer = pointer.right
    if last == "left":
        pointer.left = TreeNode(value)
    else:
        pointer.right = TreeNode(value)
    return root


def parse_string(root, st):
    key = st.split("=")[0]
    value = st.split("=")[1]
    pos = key.split(".")
    create_tree(pos, int(value), root)
    return root


def get_root(string):
    commands = string.split("hetan")
    commands.pop()
    val = int(commands[0].split("=")[1])
    commands = commands[1:]
    root = TreeNode(val)
    for command in commands:
        parse_string(root, command)
    return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)

sol = Solution()
st = "root"
print(get_string(root, st))
a = get_root(
    "root=1hetanroot.left=2hetanroot.right=3hetanroot.right.left=4hetanroot.right.left.left=6hetanroot.right.left.right=7hetanroot.right.right=5hetan"
)

print("hety")
