from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = ListNode(404, head)
        current = head
        just_before = fake

        while current:
            # move current as far as possible as long as its value is the same
            while current.next and current.next.val == current.val:
                current = current.next

            # if the range is greater than 1 we delete the whole range of duplicates
            # we check this by comparing the just_before anchor's next to current
            if just_before.next != current:
                just_before.next = current.next
            else:
                # if the range length is 1 we don't delete and move the just_before pointer
                just_before = current

            current = current.next

        return fake.next