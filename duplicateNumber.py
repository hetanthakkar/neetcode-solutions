class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.visited=False


class LinkedList:
    def __init__(self):
        self.head = None
        self.duplicate=None

    def insert(self, value):
        if self.head==None:
            self.head=Node(value)
        else:
            temp=self.head
            while(temp.next!=None):
                if(temp.value==value):
                    self.duplicate=value
                temp=temp.next
            if temp.value==value:
                self.duplicate=value
            temp.next=Node(value)

    def print(self):
        current = self.head
        while current:
            print(current.value)
            
            current = current.next

def find(nums):
    sum=0
    t=len(nums)-1
    for i in nums:
        sum=sum+i
    return int(sum-((t*(t+1))/2))
    

    # l1.insert(n)
# l1=LinkedList()
num=[1,3,4,2,2]

# l1.print()
print(find(num))