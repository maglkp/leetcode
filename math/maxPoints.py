from typing import List, Tuple, Optional


class Solution:

    def is_on_line(self, p1, p2, p3, epsilon=1e-9):
        # Compare slopes (dy/dx) using cross product to avoid division
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return abs((y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)) < epsilon

    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)

        # generate list of all point pair combinations
        pairs = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                pairs.append([points[i], points[j]])

        max_count = 0
        for pair in pairs:
            count = 2
            for point in points:
                if pair[0] != point and pair[1] != point and self.is_on_line(pair[0], pair[1], point):
                    count += 1
            max_count = max(max_count, count)

        return max_count


points = [[1, 1], [2, 2], [3, 3]]
s = Solution()
print(s.maxPoints(points))
