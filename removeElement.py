from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_ix = 0

        for element in nums:
            if val != element:
                nums[write_ix] = element
                write_ix += 1

        return write_ix


s = Solution()
nums = [3, 2, 2, 3, 1]
k = s.removeElement(nums, 3)
print(k)
print(nums)
