from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        last_interval_outside = self.find_last_interval_before_new_bts(intervals, newInterval)

        intervals_merged = intervals[:last_interval_outside + 1]
        ix = last_interval_outside + 1
        current = newInterval
        while ix < len(intervals) and self.overlaps(current, intervals[ix]):
            current = self.merge(intervals[ix], current)
            ix += 1
        intervals_merged.append(current)
        intervals_merged.extend(intervals[ix:])

        return intervals_merged

    def overlaps(self, current: List[int], new: List[int]) -> bool:
        return new[0] <= current[1]

    def merge(self, current: List[int], new: List[int]) -> List[int]:
        return [min(current[0], new[0]), max(current[1], new[1])]

    def find_last_interval_before_new_bts(self, intervals: List[List[int]], newInterval: List[int]) -> int:
        if intervals[0][1] >= newInterval[0]:
            return -1

        left = 0
        right = len(intervals) - 1
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][1] < newInterval[0]:
                left = mid + 1
            else:
                right = mid

        if intervals[left][1] < newInterval[0]:
            return left
        if intervals[right][1] < newInterval[0]:
            return right
        return left - 1


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

intervals = [[1, 5]]
newInterval = [6, 8]

#intervals = [[2, 6], [7, 9]]
#newInterval = [15, 18]
s = Solution()
print(s.insert(intervals, newInterval))
