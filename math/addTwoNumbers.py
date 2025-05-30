from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbersAcc(l1: Optional[ListNode], l2: Optional[ListNode], acc: int, prev: Optional[ListNode] = None, start: Optional[ListNode] = None) -> \
        Optional[ListNode]:
    if l1 is None:
        v1 = 0
    else:
        v1 = l1.val

    if l2 is None:
        v2 = 0
    else:
        v2 = l2.val

    val = v1 + v2 + acc
    if val > 9:
        acc = 1
        val -= 10
    else:
        acc = 0

    if start is None:
        newnode = ListNode(val)
    else:
        newnode = start
        newnode.val = val
    if prev is not None:
        prev.next = newnode

    if l1 is None:
        n1 = None
    else:
        n1 = l1.next

    if l2 is None:
        n2 = None
    else:
        n2 = l2.next

    if (n1 is None or n2 is None) and acc == 0:
        return newnode

    return addTwoNumbersAcc(n1, n2, acc, newnode)


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    node = ListNode()
    addTwoNumbersAcc(l1, l2, 0, None, node)
    return node


#l1 = ListNode(2, ListNode(4, ListNode(3)))
#l2 = ListNode(5, ListNode(6, ListNode(4)))
l1 = ListNode(2, ListNode(3))
l2 = ListNode(5, ListNode(6))
aa = addTwoNumbers(l1, l2)
print(aa)
