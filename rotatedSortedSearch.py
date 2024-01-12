# 16.5 min
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        current = nums[0]
        # nums is sorted but rotated, find the pivot point
        for pivot_ix in range(len(nums)):
            if nums[pivot_ix] < current:
                break
            current = nums[pivot_ix]

        # split array into 2 based on pivot point
        left = nums[:pivot_ix]  # exclusive
        right = nums[pivot_ix:]  # includes pivot

        # search left and right
        left_ix = self.binary_search(left, target)
        if left_ix != -1:
            return left_ix
        right_ix = self.binary_search(right, target)
        if right_ix == -1:
            return -1

        target_ix = right_ix + len(left)
        return target_ix

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

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

s = Solution()
ix = s.search(nums, target)
print(ix)
