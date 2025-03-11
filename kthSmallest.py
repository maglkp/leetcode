# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # parents = dict()
        counter = []
        kth = []

        def dfs(node):

            if kth:
                return

            if not node.left and not counter:
                counter.append(k)

            # in order traversal
            if node.left:
                dfs(node.left)

            if counter and not kth:
                counter[0] -= 1
                if counter[0] == 0:
                    kth.append(node.val)

            if node.right:
                dfs(node.right)

        dfs(root)
        return kth[0]
