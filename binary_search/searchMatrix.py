from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        N = m * n

        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            mid_m, mid_n = self.linear_to_matrix_ix(mid, n)

            if matrix[mid_m][mid_n] == target:
                return True
            elif matrix[mid_m][mid_n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def linear_to_matrix_ix(self, i: int, n: int):
        m_ix = i // n
        n_ix = i % n
        return m_ix, n_ix


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

s = Solution()
print(s.searchMatrix(matrix, target))
