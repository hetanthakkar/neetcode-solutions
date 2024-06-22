from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            p1 = head
            p2 = head.next
            p3 = p2.next
            while p2:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
            head.next = None
            head = p1
        return head

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        array1 = []
        array2 = []
        l1 = ListNode(float("inf"))
        l2 = ListNode(float("inf"))
        temp = list1
        while temp:
            array1.append(temp.val)
            if not temp.next:
                break
            temp = temp.next

        temp.next = l1
        temp = list2
        while temp:
            array2.append(temp.val)
            if not temp.next:
                break
            temp = temp.next
        temp.next = l2
        array3 = array1 + array2
        l = 0
        r = len(array3) - 1
        m = l + (r - l) // 2
        print(self.merge(array1, array2))
        head = create_linked_list(self.merge(array1, array2))
        return head

    def hasCycle(self, head: Optional[ListNode]):
        slow_pointer = head
        fast_pointer = head
        while True:
            slow_pointer = slow_pointer.next.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer.val != fast_pointer.val:
                return True

    def reorderList(self, head: Optional[ListNode]):
        temp_head = head
        right_pointer = head
        size = 0
        while True:
            if not temp_head:
                break
            else:
                temp_head = temp_head.next
                size += 1

        targetSize = size // 2 + 1

        count = 0
        count1 = 0
        right = None
        if head:
            while count1 < targetSize - 1:
                count1 += 1
                right_pointer = right_pointer.next
        # print(right_pointer.val, "hey")
        # print_linked_list(right_pointer)
        if head.next is None:
            return head
        if head:
            p1 = head
            p2 = head.next
            p3 = p2.next
            while count < targetSize - 2 and p2:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
                count += 1

            head.next = None
            head = p1
        left_pointer = head
        print(left_pointer.val)
        print_linked_list(right_pointer)
        print_linked_list(left_pointer)
        if size % 2 == 1:
            to_append = ListNode(right_pointer.val)
            right_pointer = right_pointer.next
        to_reverse = right_pointer
        while right_pointer is not None and left_pointer is not None:
            print(right_pointer.val, left_pointer.val)

            temp = right_pointer.next
            node = ListNode(left_pointer.val)
            right_pointer.next = node
            node.next = temp
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next
            if right_pointer.next is not None:
                right_pointer = right_pointer.next
        if size % 2 == 1:
            right_pointer.next = to_append
        print_linked_list(to_reverse)
        return self.reverseList(to_reverse)

    def remove_nth_node(self, head: Optional[ListNode], n: int):
        if head.next is None and n > 0:
            return None

        count = 0
        target = n
        original = head
        front_pointer = head
        rear_pointer = head
        while count < target and head.next:
            # if front_pointer.next is None:
            #     return ListNode(front_pointer.val)
            front_pointer = front_pointer.next
            count += 1
        counter1 = 0
        if front_pointer:
            while front_pointer.next is not None:
                counter1 += 1
                front_pointer = front_pointer.next
                rear_pointer = rear_pointer.next
        if counter1 == 0:
            print("counter", rear_pointer.val)

        rear_pointer.next = rear_pointer.next.next
        return original


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(" -> ".join(map(str, values)))


values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
values2 = [1, 2]
head1 = create_linked_list(values1)
head2 = create_linked_list(values2)
solution = Solution()
# reversed_head = solution.reverseList(head1)
# merged_list = solution.mergeTwoLists(head1, head2)
print_linked_list(solution.remove_nth_node(head2, 1))
# print_linked_list(solution.reorderList(head1))

# print_linked_list(merged_list)
3241

1423
