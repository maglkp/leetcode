from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        current_sum = 0
        min_len = len(nums) + 1

        while l <= r < len(nums):
            current_sum += nums[r]
            if current_sum >= target:
                min_len = min(min_len, r - l + 1)
                current_sum -= nums[l]
                current_sum -= nums[r]
                l += 1
            else:
                r += 1

        return min_len if min_len != len(nums) + 1 else 0


target, nums = 7, [2, 3, 1, 2, 4, 3]
nums = [1, 1, 1, 1, 1, 1, 1, 1]
target = 11

s = Solution()
print(s.minSubArrayLen(target, nums))
