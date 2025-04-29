from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nxt = head.next
        head.next = None

        while nxt:
            new_nxt = nxt.next
            nxt.next = head
            head = nxt
            nxt = new_nxt

        return head




