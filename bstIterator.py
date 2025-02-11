from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.vals = deque()
        node = root
        while node:
            self.vals.append(node)
            node = node.left

    def next(self) -> int:
        next_node = self.vals.pop()

        node = next_node.right
        while node:
            self.vals.append(node)
            node = node.left

        return next_node.val

    def hasNext(self) -> bool:
        return len(self.vals) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
