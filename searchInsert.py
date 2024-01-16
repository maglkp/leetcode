# 45min
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0

        bin_ix = self.binary_search(nums, target)
        if nums[bin_ix] == target:
            return bin_ix
        if nums[bin_ix] < target:
            return bin_ix + 1
        if nums[bin_ix] > target:
            return bin_ix

    def binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return mid


nums = [1, 3, 5, 6]
target = 7
# nums = [1, 3, 5, 6]
# target = 2
nums = [1, 3]
target = 2

nums = [1, 3, 5, 6]
target = 0
s = Solution()
r = s.searchInsert(nums, target)
print(r)
