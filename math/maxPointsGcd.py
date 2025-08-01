from collections import defaultdict
from typing import List
from math import gcd


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        max_count = 0
        for i in range(len(points)):
            p1 = points[i]
            slopes = defaultdict(int)
            for j in range(i + 1, len(points)):
                p2 = points[j]
                divisor = gcd((p2[1] - p1[1]), (p2[0] - p1[0]))
                dx = (p2[1] - p1[1]) / divisor
                dy = (p2[0] - p1[0]) / divisor

                if dy < 0:
                    dx, dy = -dx, -dy

                if dx == 0:
                    slope = (1, 0)
                elif dy == 0:
                    slope = (0, 1)
                else:
                    slope = (dx, dy)

                slopes[slope] += 1
            if slopes:
                max_count = max(max_count, max(slopes.values()) + 1)

        return max_count


points = [[1, 1], [2, 2], [3, 3]]
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
s = Solution()
print(s.maxPoints(points))
