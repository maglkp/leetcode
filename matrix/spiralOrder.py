from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        RIGHT = 0
        DOWN = 1
        LEFT = 2
        UP = 3

        m, n = len(matrix), len(matrix[0])
        printed = [0] * (m * n)

        direction = RIGHT
        i = j = 0
        ix = 0
        while ix < m * n:
            printed[ix] = matrix[i][j]
            if direction == RIGHT:
                if j < n - i - 1:
                    j += 1
                else:
                    direction = DOWN
                    i += 1
            elif direction == DOWN:
                if i < m - (n - j):
                    i += 1
                else:
                    direction = LEFT
                    j -= 1
            elif direction == LEFT:
                if j > m - i - 1:
                    j -= 1
                else:
                    direction = UP
                    i -= 1
            elif direction == UP:
                if i > j + 1:
                    i -= 1
                else:
                    direction = RIGHT
                    j += 1
            ix += 1

        return printed


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = Solution()
print(s.spiralOrder(matrix))
