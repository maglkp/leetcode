from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return head
        current = head
        n = 0
        while current:
            n += 1
            current = current.next

        return self.mergeSort(head, n)

    def mergeSort(self, node: ListNode, data_len) -> ListNode:
        if data_len < 2:
            node.next = None
            return node
        q = data_len // 2

        right = node
        for _ in range(q):
            right = right.next

        left = self.mergeSort(node, q)
        right = self.mergeSort(right, data_len - q)
        return self.merge(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:

        fake = ListNode()
        head = fake

        while left or right:
            if left and right:
                if left.val < right.val:
                    head.next = left
                    left = left.next
                else:
                    head.next = right
                    right = right.next
            elif left:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next

        return fake.next

s = Solution()
head = ListNode(4, ListNode(2))
sort_list = s.sortList(head)
print(sort_list)