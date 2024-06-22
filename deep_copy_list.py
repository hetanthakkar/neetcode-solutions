class ListNode:
    def __init__(self, val=0, next=None,random=None):
        self.val = val
        self.next = next
        self.random = random

class DuplicateList:
    def __init__(self):
        self.mapping1={}
        self.mapping2={}

    def create_linked_list(self, values, randoms):
        if not values:
            return None
        head = ListNode(values[0])
        self.mapping1[randoms[0]] = head
        self.mapping2[head] = randoms[0]
        current = head
        for index in range(1, len(values)):
            current.next = ListNode(values[index])
            self.mapping1[randoms[index]] = current.next
            self.mapping2[current.next] = randoms[index]
            current = current.next
        return head

    def copyRandomList(self,head):
        if not head:
            return None
        
        values=[]
        randoms=[]
        
        while head:
            values.append(head.val)
            randoms.append(head)
            head=head.next
        
        clone_head=self.create_linked_list(values,randoms)
        
        while clone_head.next:
            if self.mapping2[clone_head]==None:
                clone_head.random=None
            else:
                clone_head.random=self.mapping1[self.mapping2[clone_head].random]
            clone_head=clone_head.next
        
        return clone_head