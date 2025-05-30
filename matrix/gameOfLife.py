from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def getNeighbors(i, j):
            for x, y in ((i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                         (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)):
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        for i in range(m):
            for j in range(n):
                if board[i][j] % 10 == 1:
                    for x, y in getNeighbors(i, j):
                        board[x][y] += 10

        for i in range(m):
            for j in range(n):
                cell = board[i][j]
                # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                if cell == 1 or cell == 11:
                    board[i][j] = 0
                # Any live cell with two or three live neighbors lives on to the next generation.
                elif cell == 21 or cell == 31:
                    board[i][j] = 1
                # Any live cell with more than three live neighbors dies, as if by over-population.
                elif cell == 41 or cell == 51 or cell == 61 or cell == 71 or cell == 81:
                    board[i][j] = 0
                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                elif cell == 30:
                    board[i][j] = 1
                else:
                    board[i][j] = 0


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
s = Solution()
s.gameOfLife(board)
print(board)
# [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
