from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        MARKER = 2 ** 31

        for i in range(m):
            if any(matrix[i][j] == 0 for j in range(n)):
                for j in range(n):
                    if matrix[i][j] != 0:
                        matrix[i][j] = MARKER

        for j in range(n):
            if any(matrix[i][j] == 0 for i in range(m)):
                for i in range(m):
                    if matrix[i][j] != 0:
                        matrix[i][j] = MARKER

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == MARKER:
                    matrix[i][j] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s = Solution()
s.setZeroes(matrix)
print(matrix)
