from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        # get length of list
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1
        last = curr

        k = k % n
        if k == 0:
            return head

        # advance head n-1-k times, current will be the new last element
        curr = head
        for _ in range(n-1-k):
            curr = curr.next

        # cut the connection right after current
        new_head = curr.next
        curr.next = None

        # connect old last node to old head
        last.next = head

        # return new head which is one past current
        return new_head

