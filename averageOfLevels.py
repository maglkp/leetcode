from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        bfs = deque()
        bfs.append(root)
        level_averages = []

        while bfs:
            # process all nodes at the same level
            level_len = len(bfs)
            avg = 0.0

            # remove level_len nodes and add their children
            for i in range(level_len):
                node = bfs.popleft()
                avg += node.val
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)
            level_averages.append(avg / level_len)

        return level_averages
