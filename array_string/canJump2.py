from typing import List, Set


class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        ix = 0
        current = nums[0]
        jumps = 1
        while ix < len(nums) - 1:

            how_many_steps_more = len(nums) - 1 - ix
            if nums[ix] > current and how_many_steps_more > current:
                jumps += 1
                current = nums[ix]
            current -= 1
            ix += 1

        return jumps


s = Solution()
nums = [1]
nums = [3, 3, 1, 0, 4]
nums = [2, 3, 1]
nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
# exp = 2
print(s.jump(nums))
