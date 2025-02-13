# Definition for a Node.
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        bfs = deque()
        bfs.append(root)

        right_view = []

        while bfs:
            # process all nodes at the same level
            level_len = len(bfs)
            right_view.append(bfs[-1].val)

            # remove level_len nodes and add their children
            for i in range(level_len):
                node = bfs.popleft()
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)

        return right_view
