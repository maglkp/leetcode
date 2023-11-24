from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(-1, head)
        section_before = dummy
        section_end = self.get_k_forward(dummy, k)
        while section_end is not None:
            # revert section
            section_after = section_end.next
            section_start = section_before.next
            self.revert_node_and_continue(section_start.next, section_start, k - 1)

            # connect before and after
            section_before.next = section_end
            section_start.next = section_after

            # get next section
            section_end = self.get_k_forward(section_start, k)
            # new section before is current section's end
            section_before = section_start

        return dummy.next

    def get_k_forward(self, node: ListNode, k: int):
        for i in range(k):
            if node.next is None:
                return None
            node = node.next
        return node

    def revert_node_and_continue(self, current: ListNode, prev: ListNode, reverts_left: int):
        if reverts_left == 0:
            return

        node_next = current.next
        current.next = prev
        self.revert_node_and_continue(node_next, current, reverts_left - 1)


s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
#list1 = ListNode(1, ListNode(2, ListNode(3)))
sw = s.reverseKGroup(list1, 1)
print(sw)
