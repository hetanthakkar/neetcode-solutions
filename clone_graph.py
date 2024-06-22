from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def generate_list(node):
    mapping={}
    seen={}
    q=deque()
    re=Node(node.val)
    mapping[node]=re
    seen[re.val]=re
    hey=[]
    n1=None
    q.appendleft(node)
    while q:
        temp=[]
        temp1=q.pop()
        hey.append(temp1)
        for neighbor in temp1.neighbors:
            if neighbor.val not in seen:
                n1=Node(neighbor.val)
            else:
                n1=seen[neighbor.val]
            seen[neighbor.val]=n1
            mapping[temp1].neighbors.append(n1)
            mapping[neighbor]=n1
            temp.append(n1)
            if neighbor not in q and neighbor not in hey:
                q.appendleft(neighbor)    

    return re
class Solution:
    def cloneGraph(self, node):
        if not node:
            return node
        adj_list=generate_list(node)
        return adj_list

       
