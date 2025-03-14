from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])

        def bfs(i, j):
            stack = deque()
            stack.append((i, j))
            all_valid = True
            region = set()

            while stack:
                i, j = stack.pop()
                if i not in range(n) or j not in range(m) or board[i][j] != "O":
                    continue
                board[i][j] = "?"
                region.add((i, j))
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    all_valid = False
                stack.append((i - 1, j))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
                stack.append((i, j + 1))

            for (a, b) in region:
                board[a][b] = "X" if all_valid else "O"

        for i in range(n):
            for j in range(m):
                # this causes redundant traversals cause board is reversed to Os if it is surrounded
                # extra visited set should be used for better efficiency
                if board[i][j] == "O":
                    bfs(i, j)
