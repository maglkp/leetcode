from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        #current = head

        # advance head left - 1 times
        for _ in range(left - 1):
            current = current.next

        # one before left
        one_before_left = current
        left_node = current.next

        # remove the link just before the start of the sublist to be reversed
        nxt = current.next
        current.next = None

        # set the initial pointers
        current = nxt
        nxt = nxt.next

        for _ in range(right - left):
            new_nxt = nxt.next
            nxt.next = current
            current = nxt
            nxt = new_nxt

        one_past_right = new_nxt

        # connect reversed sublist, current being last element of the reversed sublist
        one_before_left.next = current
        left_node.next = one_past_right

        return dummy.next
