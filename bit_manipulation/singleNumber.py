from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0
        for num in nums:
            acc ^= num

        return acc
