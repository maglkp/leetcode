from typing import List, Set


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ix = 0
        current = nums[0]
        while ix < len(nums):
            current = max(current, nums[ix])
            if current <= 0:
                break
            current -= 1
            ix += 1

        return ix >= len(nums) - 1


s = Solution()
nums = [2, 3, 1, 1, 0]
#nums = [3, 2, 1, 0, 4]
print(s.canJump(nums))
