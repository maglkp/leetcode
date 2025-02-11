# Definition for a binary tree node.
from typing import Optional

# DFS with scoped var
# DFS with stack, return 1 if node is leaf, 0 otherwise and sum to top
# BFS only count last level (no child for first element)
# total elements in complete tree = 2**h - 1
# total elements in a row at level h = 2**(h - 1)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = [0]

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            count[0] += 1
            dfs(node.right)

        dfs(root)
        return count[0]

