
# add all the connected nodes to queue
# remove the element from queue
# once you remove the element, add connected nodes to the queue
# if you encounter A-1 when you are enqueing the element return true
# print(first_connected_nodes)

from collections import deque

def find_edge(A,B):
    q=deque()
    graph = [[0 for _ in range(A)] for _ in range(A)]
    for i in B:
        graph[i[0]-1][i[1]-1]=1

    first_connected_nodes=graph[0]

    for i in range(0,len(first_connected_nodes)):
        if(first_connected_nodes[i]==1):
            q.appendleft(i)

    while q:
        removed=q.pop()
        connected=graph[removed]
        for i in range(0,len(connected)):
            if(connected[i]==1):
                if(i==A-1):
                    return True
                q.appendleft(i)
    return False

print(find_edge(6,[
  [0,1],
  [1, 2],
  [2,4],
  [3,1],
#   [4, 3],
  [4, 5]
]))