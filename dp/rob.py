from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.rob_dp(nums, {})

    def rob_dp(self, nums: List[int], memo: dict) -> int:
        if len(nums) in memo:
            return memo[len(nums)]

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        n1 = self.rob_dp(nums[1:], memo)
        n2 = nums[0] + self.rob_dp(nums[2:], memo)
        n12 = max(n1, n2)
        memo[len(nums)] = n12
        return n12
