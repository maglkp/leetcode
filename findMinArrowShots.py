from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 2:
            return len(points)

        # sort the points according to start time
        points.sort(key=lambda x: x[0])

        # initialize the number of arrow shots to len of points and decrease for every overlap
        arrow_shots = len(points)
        current = points[0]
        for ix in range(1, len(points)):
            if self.overlaps(current, points[ix]):
                arrow_shots -= 1
                current = self.get_overalapping_range(current, points[ix])
            else:
                current = points[ix]

        return arrow_shots

    def overlaps(self, predecessor: List[int], new: List[int]) -> bool:
        return new[0] <= predecessor[1]

    def get_overalapping_range(self, predecessor: List[int], new: List[int]) -> List[int]:
        return [max(predecessor[0], new[0]), min(predecessor[1], new[1])]


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
points = [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
s = Solution()
print(s.findMinArrowShots(points))
