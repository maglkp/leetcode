from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def lengthOfLIS_invalid(self, nums: List[int]) -> int:

        max_lis = 0
        for i in range(len(nums)):
            lis = 1
            max_el = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > max_el:
                    max_el = nums[j]
                    lis += 1

            max_lis = max(max_lis, lis)

        return max_lis


s = Solution()
#nums = [0, 1, 0, 3, 2, 3]
nums = [3, 10, 2, 1, 20]
nums = [10, 20, 30, 1, 25]
print(s.lengthOfLIS(nums))
