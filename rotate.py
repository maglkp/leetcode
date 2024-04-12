from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        if len(nums) % k == 0:
            for start_ix in range(k):
                ix = start_ix
                value_copy = nums[ix]
                while ix + k < len(nums):
                    temp = nums[ix + k]
                    nums[ix + k] = value_copy
                    value_copy = temp
                    ix += k
                nums[start_ix] = value_copy
        else:
            replace_count = 0
            start_ix = 0

            while replace_count < len(nums):
                end_ix = (start_ix + k) % len(nums)
                value_copy = nums[start_ix]

                while end_ix != start_ix and replace_count < len(nums):
                    temp = nums[end_ix]
                    nums[end_ix] = value_copy
                    value_copy = temp
                    end_ix = (end_ix + k) % len(nums)
                    replace_count += 1

                if replace_count < len(nums):
                    nums[start_ix] = value_copy
                    replace_count += 1

                start_ix += 1


nums = [1, 2, 3, 4, 5, 6]
k = 4
s = Solution()
s.rotate(nums, k)
print(nums)
