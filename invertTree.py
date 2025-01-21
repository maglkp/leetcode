from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        inv_left =  self.invertTree(root.right)
        inv_right = self.invertTree(root.left)
        root.left = inv_left
        root.right = inv_right

        return root
