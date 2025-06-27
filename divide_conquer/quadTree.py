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
        return self.constructLevel(grid, 0, 0, len(grid))

    def constructLevel(self, grid: List[List[int]], r0: int, c0: int, n: int) -> 'Node':

        cnt = self.countAll(grid, r0, c0, n)
        if cnt == 0:
            return Node(0, True, None, None, None, None)
        if cnt == 1:
            return Node(1, True, None, None, None, None)

        n = n // 2
        top_left = self.constructLevel(grid, r0, c0, n)
        top_right = self.constructLevel(grid, r0, c0 + n, n)
        bottom_left = self.constructLevel(grid, r0 + n, c0, n)
        bottom_right = self.constructLevel(grid, r0 + n, c0 + n, n)
        return Node(0, False, top_left, top_right, bottom_left, bottom_right)

    def countAll(self, grid: List[List[int]], r0: int, c0: int, n: int) -> int:
        # returns 0 if all cells are 0
        # returns 1 if all cells are 1
        # returns -1 if some cells are 1 and some 0
        all = 0
        for r in range(r0, r0 + n):
            for c in range(c0, c0 + n):
                cell = grid[r][c]
                if all > 0 and cell == 0:
                    return -1
                #elif cell == 1 and there was 0 before return -1
                all += cell
        if all == n * n:
            return 1
        elif all == 0:
            return 0
        else:
            return -1

    # def mergeAndConstruct_dfs(self, grid: List[List[int]], r: int, c: int, size: int) -> 'Node':
    #     if size == 1:
    #         return Node(grid[r][c], True, None, None, None, None)
    #
    #     size = size // 2
    #     top_left = self.mergeAndConstruct_dfs(grid, r, c, size)
    #     top_right = self.mergeAndConstruct_dfs(grid, r, c + size, size)
    #     bottom_left = self.mergeAndConstruct_dfs(grid, r + size, c, size)
    #     bottom_right = self.mergeAndConstruct_dfs(grid, r + size, c + size, size)
    #
    #     # merge - if all are of the same value and are leaf create just 1 new leaf node and abandon the current 4
    #     all_leaf = top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf
    #     all_same = top_left.val == top_right.val and bottom_left.val == bottom_right.val
    #     if all_leaf and all_same:
    #         return Node(top_left.val, True, None, None, None, None)
    #     # otherwise create non leaf node and attach above 4
    #     else:
    #         return Node(0, False, top_left, top_right, bottom_left, bottom_right)


grid = [[1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0]]

s = Solution()
print(s.construct(grid))