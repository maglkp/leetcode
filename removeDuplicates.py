from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_ix = 0
        last_value = None

        for element in nums:
            if last_value != element:
                last_value = element
                nums[write_ix] = element
                write_ix += 1

        return write_ix


s = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = s.removeDuplicates(nums)
print(k)
print(nums)
