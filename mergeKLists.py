# O(nk) n - num of all elements, k - num of lists
# can knock it down to O(nlogk) if logk insertion is used using priority queues

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
        lists.sort(key=cmp_to_key(self.lower_head))
        dummy = ListNode()
        self.take_and_continue(lists, dummy)

        return dummy.next

    def take_and_continue(self, lists: List[Optional[ListNode]], current_output: ListNode) -> Optional[ListNode]:
        # remove empty lists
        #lists = list(filter(lists, lambda e: e is not None))
        lists = [e for e in lists if e is not None]

        # if no stuff left return
        if len(lists) == 0:
            return

        # take the first element, append it to output list
        next_e = lists[0]
        current_output.next = next_e

        # remove first list from lists
        head_list = lists.pop(0)

        # if there is still stuff in that list, remove element we just added
        # and insert the tail according to its first element value
        if head_list.next is not None:
            new_list = head_list.next
            new_list_val = new_list.val

            ix = 0
            is_less = False
            for ix, head_node in enumerate(lists):
                if new_list_val < head_node.val:
                    is_less = True
                    break

            if is_less:
                lists.insert(ix, new_list)
            else:
                lists.append(new_list)

        # continue
        self.take_and_continue(lists, next_e)

    def lower_head(self, x: Optional[ListNode], y: Optional[ListNode]):
        # empty elements go first
        if x is None:
            return 1
        if y is None:
            return -1
        return x.val - y.val


s = Solution()
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]

k_lists = s.mergeKLists(lists)
print(k_lists)

# lists.sort(key=lower_head)
# lists = sorted(lists, key=cmp_to_key(lower_head))


print(lists[0].val)
