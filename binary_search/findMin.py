from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        inflection = self.find_inflection(nums)
        return nums[inflection]

    def find_inflection(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if mid == len(nums) - 1:
                return 0
            if nums[mid] > nums[mid + 1]:
                inflection = mid + 1
                break

            if nums[left] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return inflection
