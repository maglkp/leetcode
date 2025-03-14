from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def bfs(i, j):
            stack = deque()
            stack.append((i, j))
            while stack:
                i, j = stack.pop()
                if i not in range(n) or j not in range(m) or grid[i][j] != "1":
                    continue
                grid[i][j] = "2"
                stack.append((i - 1, j))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
                stack.append((i, j + 1))

        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    num_islands += 1
        return num_islands


    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != "1":
                return
            grid[i][j] = "2"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        num_islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1
        return num_islands
