from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        current = head

        # advance head left-1 times
        for _ in range(left - 1):
            current = current.next

        nxt = current.next
        current.next = None

        for _ in range(right):
            new_nxt = nxt.next
            nxt.next = current
            current = nxt
            nxt = new_nxt

        return head
