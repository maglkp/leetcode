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
        return self.merge_no_dummy(left, right)

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        fake = ListNode()
        node = fake

        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next

        node.next = left or right
        return fake.next

    def merge_no_dummy(self, left: ListNode, right: ListNode) -> ListNode:
        if not left:
            return right
        if not right:
            return left

        # Initialize head to the smaller of the two nodes
        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next

        current = head

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Attach the remaining part
        current.next = left if left else right

        return head


s = Solution()
head = ListNode(4, ListNode(2))
sort_list = s.sortList(head)
print(sort_list)
