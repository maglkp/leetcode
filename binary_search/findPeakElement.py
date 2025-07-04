from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        n = len(nums)
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            mid_left = nums[mid - 1] if mid > 0 else float('-inf')
            mid_right = nums[mid + 1] if mid < n - 1 else float('-inf')
            if mid_left < mid_val > mid_right:
                return mid

            if mid_left > mid_val:
                right = mid - 1
            else:
                left = mid + 1

        raise "should always have a peak element due to constraints"


nums = [1, 2, 3, 1]
s = Solution()
print(s.findPeakElement(nums))
