from collections import deque
class Graph:
    def __init__(self,matrix):
        self.nodes=0
        self.visited={}
        self.top=0
        self.bottom=0
        self.matrix=matrix
        for i in range(0,len(matrix)):
            self.nodes=self.nodes+len(matrix[i])

        self.list=[[] for _ in range(0,self.nodes)]
        self.top=len(matrix[0])
        self.bottom=len(self.list)-len(self.matrix[len(self.matrix)-1])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                current=matrix[i][j]
                top=left=bottom=right=None

                if 0 <= i < len(matrix):
                    if 0 <= j+1 < len(matrix[0]):
                        right = matrix[i][j+1]   
                                       
                if 0 <= i+1 < len(matrix):
                    if 0 <= j < len(matrix[0]):
                        bottom = matrix[i+1][j]                                        
                if 0 <= i < len(matrix):
                    if 0 <= j-1 < len(matrix[0]):
                        left = matrix[i][j-1]
                if 0 <= i-1 < len(matrix):
                    if 0 <= j < len(matrix[0]):
                        top = matrix[i-1][j]    

                if(bottom!=None and bottom==1 and current==1):
                    self.list[i*len(matrix[i])+j].append((i+1)*len(matrix[i+1])+j)
          
                if(right != None and right==1 and current==1):
                    self.list[i*len(matrix[i])+j].append(i*len(matrix[i])+j+1)
                
                if(top != None and top==1 and current==1):
                    self.list[i*len(matrix[i])+j].append((i-1)*len(matrix[i-1])+j)  
                
                if(left != None and current==1 and left==1):
                    self.list[i*len(matrix[i])+j].append(i*len(matrix[i])+j-1)                   

    def bfs(self,src,processed,pro):
        # print(pro)
        bfs=[]
        q=deque()
        seen=set()
        seen.add(src-1)
        first_connected_nodes=self.list[src-1]
        for i in range(0,len(first_connected_nodes)):
            q.appendleft(first_connected_nodes[i])
            seen.add(first_connected_nodes[i])
        processed=[]
        bfs.append(src)
        while q:
            removed=q.pop()
            if removed+1 in pro:
                return True
            bfs.append(removed+1)
            connected=self.list[removed]
            if isinstance(connected, list):
                for i in range(0,len(connected)):
                    if  connected[i] not in seen and connected[i] not in processed:
                        processed.append(connected[i])
                        q.appendleft(connected[i])
        return bfs                          

    def number_of_island(self):
        island=[]
        processed=[]
        pro=set()
        seen=set()
        for i in range(1,len(self.list)+1):
            if i not in seen:
                row=(i-1)//self.top
                col=(i-1)%self.top
                if self.matrix[row][col]==1:
                    result=self.bfs(i,processed,pro)
                    print("Result",result)
                    island.append(result)
                    seen.update(result)
                else:
                    seen.add(i)
        print(island)
        return max(len(subarray) for subarray in island)
        # return (island)



B=[[0,0,0,0,0,0,0,0]]
# B=[
#   [1]
# ]

g1=Graph(B)
print(g1.number_of_island())
