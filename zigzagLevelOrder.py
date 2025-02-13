from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        bfs = deque()
        bfs.append(root)
        levels = []
        is_zig_zag = False

        while bfs:
            # process all nodes at the same level
            level_len = len(bfs)
            level = []

            # remove level_len nodes and add their children
            for i in range(level_len):
                node = bfs.popleft()
                level.append(node.val)

                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)

            if is_zig_zag:
                level.reverse()
            is_zig_zag = not is_zig_zag
            levels.append(level)

        return levels
