from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        inflection = self.find_inflection(nums)

        # split array into 2 based on pivot point
        left = nums[:inflection]  # exclusive
        right = nums[inflection:]  # includes pivot

        # search left and right
        left_ix = self.binary_search(left, target)
        if left_ix != -1:
            return left_ix
        right_ix = self.binary_search(right, target)
        if right_ix == -1:
            return -1

        target_ix = right_ix + len(left)
        return target_ix

    def find_inflection(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # if mid == 0:
            #     inflection = mid
            #     break
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


nums = [4, 5, 6, 7, 0, 1, 2]
nums = [1, 3]

target = 0

# nums = [3, 1]
# target = 1

s = Solution()
ix = s.search(nums, target)
print(ix)
