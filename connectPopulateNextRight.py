# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        bfs = deque()
        bfs.append(root)

        while bfs:
            # process all nodes at the same level
            level_len = len(bfs)
            for i in range(len(bfs) - 1):
                bfs[i].next = bfs[i + 1]

            # remove level_len nodes and add their children
            for i in range(level_len):
                node = bfs.popleft()
                if node.left:
                    bfs.append(node.left)
                if node.right:
                    bfs.append(node.right)

        return root