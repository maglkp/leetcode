# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, node) -> Optional[int]:
        limit = 10 ** 5 + 1
        if not node:
            return None

        l = self.dfs(node.left) or limit
        r = self.dfs(node.right) or limit

        if node.left is not None and node.right is not None:
            return min(abs(node.left.val - node.val), abs(node.right.val - node.val), l, r)
        elif node.right is not None:
            return min(abs(node.right.val - node.val), r)
        elif node.left is not None:
            return min(abs(node.left.val - node.val), l)
        else:
            return None