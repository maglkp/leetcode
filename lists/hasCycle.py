from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast_ptr_speed = 2
        slow = head
        fast = head

        while fast:
            # actually no need to check it with every move, can move fast and slow and check after
            # this also allows to identify cycle start node if that was needed
            for _ in range(fast_ptr_speed):
                fast = fast.next
                if not fast:
                    return False
                if slow == fast:
                    return True
            slow = slow.next

        return False