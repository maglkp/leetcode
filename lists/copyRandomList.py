from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        # create a copy of the list without random pointers
        # map values to new nodes
        old_to_new = {}
        cur = head

        # do the first copy manually outside of loop to capture head
        new_node = Node(cur.val, None, None)
        head_copy = new_node
        cur_copy = new_node
        old_to_new[cur] = new_node
        cur = cur.next

        while cur:
            new_node = Node(cur.val, None, None)
            cur_copy.next = new_node
            old_to_new[cur] = new_node
            cur_copy = cur_copy.next
            cur = cur.next

        # now copy random pointers
        cur = head
        cur_copy = head_copy
        while cur:
            if cur.random:
                cur_copy.random = old_to_new[cur.random]
            cur = cur.next
            cur_copy = cur_copy.next

        return head_copy

