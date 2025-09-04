from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.min_path_sum_dp(grid, 0, 0, len(grid[0]) - 1, len(grid) - 1, {})

    def min_path_sum_dp(self, grid: List[List[int]], r: int, c: int, right_moves: int, down_moves: int,
                        memo: dict) -> int:

        if (r, c) in memo:
            return memo[(r, c)]

        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            # could add to memo here too
            return grid[r][c]

        down, right = float('inf'), float('inf')
        if right_moves > 0:
            right = grid[r][c] + self.min_path_sum_dp(grid, r, c + 1, right_moves - 1, down_moves, memo)
        if down_moves > 0:
            down = grid[r][c] + self.min_path_sum_dp(grid, r + 1, c, right_moves, down_moves - 1, memo)

        v = min(right, down)
        #print(f"{r} {c}: {v}")
        memo[(r, c)] = v
        return v


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
s = Solution()
v = s.minPathSum(grid)
print(f"solution: {v}")
# print(v)
