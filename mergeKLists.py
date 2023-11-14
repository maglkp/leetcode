from typing import Optional, List
from functools import cmp_to_key


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1 sort lists as it is with custom method
        # 2 [if there is stuff left] take the first element, append it to output list
        # 3 remove first list from lists
        # 4 insert that list according to its first element value
        # goto 2
        pass


s = Solution()
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
list1 = ListNode(10, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]


# print(s.mergeKLists(lists))

def lower_head(x: Optional[ListNode], y: Optional[ListNode]):
    if x is None:
        return -1
    if y is None:
        return 1
    return x.val - y.val


# lists.sort(key=lower_head)
#lists = sorted(lists, key=cmp_to_key(lower_head))
lists.sort(key=cmp_to_key(lower_head))

print(lists[0].val)