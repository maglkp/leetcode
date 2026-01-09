from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        max_size = 0

        # dp contains max squares of 1s starting at index
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                square_below = dp[j]
                square_right = 0 if j == n - 1 else dp[j + 1]
                min_square = min(square_below, square_right)
                current = int(matrix[i][j])

                if min_square == 0:
                    dp[j] = current
                else:
                    ix = i + min_square, j + min_square

                    missing_element = int(matrix[ix[0]][ix[1]] if ix[0] < m and ix[1] < n else "0")
                    if missing_element == 1 and current == 1:
                        dp[j] = min_square + 1
                    elif current == 1:
                        dp[j] = min_square
                    else:
                        dp[j] = current

                max_size = max(max_size, dp[j])

        return max_size * max_size


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
matrix = [["0", "0", "1", "0"],
          ["1", "1", "1", "1"],
          ["1", "1", "1", "1"],
          ["1", "1", "1", "0"],
          ["1", "1", "0", "0"],
          ["1", "1", "1", "1"],
          ["1", "1", "1", "0"]]
s = Solution()
print(s.maximalSquare(matrix))
