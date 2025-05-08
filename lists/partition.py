from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if head is None:
            return head

        # create two fake nodes to hold lesser and greater or equal values
        lt_head = lt = ListNode(404)
        ge_head = ge = ListNode(404)

        node = head
        while node:
            if node.val < x:
                lt.next = node
                lt = lt.next
            else:
                ge.next = node
                ge = ge.next

            next_node = node.next
            node.next = None
            node = next_node

        # connect the two lists, one has to be non-empty
        if not lt_head.next:
            return ge_head.next

        lt.next = ge_head.next
        return lt_head.next
