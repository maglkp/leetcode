from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: (x[0], x[1]))
        merged = []
        current = intervals[0]
        for ix in range(1, len(intervals)):
            if intervals[ix][0] <= current[1] :
                current[1] = max(current[1], intervals[ix][1])
            else:
                merged.append(current)
                current = intervals[ix]

            if ix == len(intervals) - 1:
                merged.append(current)

        return merged


intervals = [[1, 4], [1, 3], [2, 6], [8, 10], [15, 18]]
s = Solution()
print(s.merge(intervals))
