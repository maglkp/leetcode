# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


        self.visit_and_flatten(root)

    def visit_and_flatten(self, node: Optional[TreeNode]) -> Optional[TreeNode]:

        if not node:
            return None

        last_on_left = self.visit_and_flatten(node.left)
        last_on_right = self.visit_and_flatten(node.right)

        # put the flattened left side on the right between root and flattened right side and clear root.left
        if last_on_left:
            last_on_left.right = node.right
            node.right = node.left
            node.left = None

        return last_on_right or last_on_left or node