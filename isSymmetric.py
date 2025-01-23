from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirrorImage(root.left, root.right)

    def isMirrorImage(self, node_on_left_side, node_on_right_side):
        if node_on_left_side is None and node_on_right_side is None:
            return True
        if node_on_left_side is None or node_on_right_side is None:
            return False
        if node_on_left_side.val != node_on_right_side.val:
            return False
        return (self.isMirrorImage(node_on_left_side.left, node_on_right_side.right) and
                self.isMirrorImage(node_on_left_side.right, node_on_right_side.left))
