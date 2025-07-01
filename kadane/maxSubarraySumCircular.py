from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        non_circular = self.maxSubArray(nums)

        left = nums[0]
        max_left = left
        for i in range(1, len(nums)):
            left += nums[i]
            max_left = max(max_left, left)

        right = nums[-1]
        max_right = right
        for i in range(len(nums) - 2, -1, -1):
            right += nums[i]
            max_right = max(max_right, right)

        circular = max_left + max_right
        return max(circular, non_circular)

    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum > 0:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            max_value = max(max_value, current_sum)

        return max_value


nums = [5, -3, 5]
s = Solution()
print(s.maxSubarraySumCircular(nums))
