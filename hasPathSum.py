# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.hasSum(root, targetSum)

    def hasSum(self, node: Optional[TreeNode], targetSum: int) -> bool:
        if node is None:
            return False

        # if this is a leaf node check if sum is equal to target
        if node.left is None and node.right is None:
            return targetSum == node.val

        return self.hasPathSum(node.left, targetSum - node.val) or self.hasPathSum(node.right, targetSum - node.val)
