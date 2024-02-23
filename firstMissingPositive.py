import time
from typing import List, Dict


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        threshold = len(nums) + 1
        for ix in range(len(nums)):
            if nums[ix] <= 0:
                nums[ix] = threshold

        for ix in range(len(nums)):
            num_to_check = nums[ix]
            if num_to_check < 0:
                num_to_check *= -1
            if num_to_check < threshold:
                value_present_ix = num_to_check - 1
                if nums[value_present_ix] > 0:
                    nums[value_present_ix] *= -1

        for ix in range(len(nums)):
            if nums[ix] > 0:
                return ix + 1

        return threshold


nums = [7, 8, 9, 11, 12]
#nums = [3, 4, -1, 1]
s = Solution()
print(s.firstMissingPositive(nums))
