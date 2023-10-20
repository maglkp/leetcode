# backtracking
# can also add dummy node at the beginning to get rid of edge cases

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return None

        right = left = head
        size = 1
        for i in range(n):
            if right.next is not None:
                right = right.next
                size += 1

        while right.next is not None:
            right = right.next
            left = left.next

        if left == head and size == n:
            return head.next
        else:
            left.next = left.next.next
            return head

s = Solution()
#head = ListNode(1, ListNode(2, ListNode(12)))
head = ListNode(1, ListNode(2))
head = s.removeNthFromEnd(head, 1)
print(head)
