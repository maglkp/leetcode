# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# use 2 running pointers
from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while True:
        current = numbers[left] + numbers[right]
        if current == target:
            return [left + 1, right + 1]
        if current > target:
            if left + 1 < right:
                left += 1
            if left + 1 < right:
                right -= 1
        # it's still smaller, do we push left or right one first?
        else:
            if right == len(numbers) - 1 and left + 1 < right:
                left += 1
            elif right < len(numbers) - 1:
                right += 1


#print(twoSum("", [5, 25, 75], 100))
#print(twoSum("", [3, 24, 50, 79, 88, 150, 345], 200))
print(twoSum("", [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997], 542))
