from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummi = ListNode(-1, head)
        self.swap_and_continue(dummi)
        return dummi.next

    def swap_and_continue(self, previous: ListNode):
        if previous.next is None or previous.next.next is None:
            return

        node1 = previous.next
        node2 = previous.next.next
        node_next = previous.next.next.next

        previous.next = node2
        node2.next = node1
        node1.next = node_next

        self.swap_and_continue(node1)


s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sw = s.swapPairs(list1)
print(sw)
