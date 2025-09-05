from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n, m = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        if m == 1 and n == 1:
            return 1

        zeroes = [0] * m
        for i in range(n):
            for j in range(m):
                current_row = obstacleGrid[i]
                previous_row = obstacleGrid[i - 1] if i > 0 else zeroes

                if i == 0 and j == 0:
                    current_row[j] = 1
                    continue

                from_left = current_row[j - 1] if j > 0 else 0
                from_top = previous_row[j]

                paths_to_this_cell = (from_left + from_top) if current_row[j] != 1 else 0
                current_row[j] = paths_to_this_cell

        return current_row[-1]


obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid))
