# 45min
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_middle_ix = self.binary_search(nums, target)
        if target_middle_ix == -1:
            return [-1, -1]

        # find last target value after target_middle_ix by exponential search
        target_last_ix = target_middle_ix
        while target_last_ix < len(nums) - 1 and nums[target_last_ix] == target:
            exponent = 0
            # exponential search
            while target_last_ix + 2 ** exponent < len(nums) - 1 and nums[target_last_ix + 2 ** exponent] == target:
                exponent += 1

            if exponent > 0:
                exponent -= 1
            target_last_ix += 2 ** exponent

        if nums[target_last_ix] != target:
            target_last_ix -= 1

        # find first target value before target_middle_ix by exponential search
        target_first_ix = target_middle_ix
        while target_first_ix > 0 and nums[target_first_ix] == target:
            exponent = 0
            # backwards exponential search
            while target_first_ix - 2 ** exponent > 0 and nums[target_first_ix - 2 ** exponent] == target:
                exponent += 1

            if exponent > 0:
                exponent -= 1
            target_first_ix -= 2 ** exponent

        if nums[target_first_ix] != target:
            target_first_ix += 1

        return [target_first_ix, target_last_ix]

    def binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1


nums = [5, 7, 7, 8, 8, 10]
nums = [5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10]  # 0..13
nums = [5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]  # 0..12
nums = [8, 8, 8, 8, 8, 8, 8, 8]  # 0..7
target = 8
s = Solution()
r = s.searchRange(nums, target)
print(r)
