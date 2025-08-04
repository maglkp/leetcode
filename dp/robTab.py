from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        tab = [0, nums[0], max(nums[0], nums[1])] + [0] * (len(nums) - 2)
        for i in range(3, len(nums) + 1):
            tab[i] = max(tab[i - 1], nums[i - 1] + tab[i - 2])

        return tab[-1]