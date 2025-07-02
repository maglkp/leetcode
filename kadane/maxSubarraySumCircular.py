from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        all = sum(nums)
        min_s = self.minSubArray(nums)
        max_s = self.maxSubArray(nums)
        wrap = all - min_s

        return max(wrap, max_s) if wrap != 0 else max_s

    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_value = max(max_value, current_sum)

        return max_value

    def minSubArray(self, nums: List[int]) -> int:
        min_value = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = min(current_sum + nums[i], nums[i])
            min_value = min(min_value, current_sum)

        return min_value


nums = [5, -3, 5]
nums = [1, -2, 3, -2]
nums = [-3, -2, -3]
s = Solution()
print(s.maxSubarraySumCircular(nums))
