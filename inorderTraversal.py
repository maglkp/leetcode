# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        vals = []
        stack = deque()
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            node = stack.pop()
            vals.append(node.val)
            current = node.right

        return vals
