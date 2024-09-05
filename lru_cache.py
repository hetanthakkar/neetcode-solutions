class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.end = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.end = new_node

    def move_to_end(self, data):
        if self.end != self.head:
            if not self.head:
                return
            if self.head.data == data:
                self.end.next = self.head
                self.head = self.head.next
                self.head.next = None
                return
            current_node = self.head

            while current_node.next and current_node.next.data != data:
                current_node = current_node.next
            if current_node.next:
                self.end = current_node.next
                current_node.next = current_node.next.next

    def remove_first(self):
        if not self.head:
            return
        removed_value = self.head.data
        self.head = self.head.next
        return removed_value


class LRUCache:

    def __init__(self, capacity):
        self.least = LinkedList()
        self.dic = {}
        self.capacity = capacity

    def get(self, key):
        if key in self.dic:
            self.least.move_to_end(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.dic:
            self.dic[key] = value
            self.least.move_to_end(key)
            return
        self.dic[key] = value
        self.least.append(key)
        if len(self.dic) > self.capacity:
            removed = self.least.remove_first()
            self.dic.pop(removed, None)


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
print(lRUCache.get(1))
lRUCache.put(3, 3)
print(lRUCache.get(2))
# lRUCache.put(4, 4)
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
