from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


s = Solution()
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(s.mergeKLists(lists))
