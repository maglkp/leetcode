from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.mergeAndConstruct(grid, 0, 0, len(grid))

    def mergeAndConstruct(self, grid: List[List[int]], r: int, c: int, size: int) -> 'Node':
        if size == 1:
            return Node(grid[r][c], True, None, None, None, None)

        size = size // 2
        top_left = self.mergeAndConstruct(grid, r, c, size)
        top_right = self.mergeAndConstruct(grid, r, c + size, size)
        bottom_left = self.mergeAndConstruct(grid, r + size, c, size)
        bottom_right = self.mergeAndConstruct(grid, r + size, c + size, size)

        # merge - if all are of the same value and are leaf create just 1 new leaf node and abandon the current 4
        all_leaf = top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf
        all_same = top_left.val == top_right.val and bottom_left.val == bottom_right.val
        if all_leaf and all_same:
            return Node(top_left.val, True, None, None, None, None)
        # otherwise create non leaf node and attach above 4
        else:
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)


