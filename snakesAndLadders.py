from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        q = deque([1])
        n = len(board)
        step = 0
        visited = set()

        while q:
            len_q = len(q)
            for _ in range(len_q):
                cell = q.popleft()
                if cell == n * n:
                    return step

                for j in range(cell + 1, min(cell + 6, n * n) + 1):
                    r, c = divmod(j - 1, n)
                    row = n - 1 - r
                    row_is_even = r % 2 == 0
                    if row_is_even:
                        col = c
                    else:
                        col = n - c - 1
                    cell_value = board[row][col]

                    new_cell = j if cell_value == -1 else cell_value
                    if new_cell not in visited:
                        q.append(new_cell)
                        visited.add(new_cell)
            step += 1
        return -1


board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]
board = [[-1,-1],[-1,3]]
board = [
    [1, 1, -1],
    [1, 1, 1],
    [-1, 1, 1]]


s = Solution()

print(s.snakesAndLadders(board))
