# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_val = [root.val]

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            max_val[0] = max(max_val[0],
                             node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        return max_val[0]

    def maxPathSum1(self, root: Optional[TreeNode]) -> int:
        path = self.maxPath(root)
        return max(path)

    # returns (current, max) for paths leading up to this node where current is current max gain between left and right
    # and max is all time max sub path for downstream paths
    def maxPath(self, node: Optional[TreeNode]) -> (int, int):

        if not node:
            return 0, 0

        if not node.left and not node.right:
            return node.val, node.val

        if (not node.left and node.right) or (node.left and not node.right):
            active_node = node.left or node.right
            downstream = self.maxPath(active_node)
            current = downstream[0] + node.val
            return current, max(downstream[1], current, node.val)

        downstream_left = self.maxPath(node.left)
        downstream_right = self.maxPath(node.right)

        current = max(node.val + downstream_left[0], node.val + downstream_right[0])
        max_downstream = max(downstream_left[1],
                             downstream_right[1],
                             downstream_left[0] + downstream_right[0] + node.val,
                             node.val,
                             current)
        return current, max_downstream
