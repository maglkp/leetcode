from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum > 0:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            #or
            #current_sum = max(current_sum + nums[i], nums[i])

            max_value = max(max_value, current_sum)

        return max_value