from typing import List, Dict


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        occurrences = {}
        for i in range(101):
            occurrences[i] = 0

        # find index of first decreasing element starting from end of list
        decreasing_ix = len(nums) - 2
        while decreasing_ix >= 0 and nums[decreasing_ix] >= nums[decreasing_ix + 1]:
            decreasing_ix -= 1

        # create an occurrences map of the non-increasing part of the list
        for ix in range(decreasing_ix + 1, len(nums)):
            occurrences[nums[ix]] += 1

        # if we find a decreasing element, swap it with one greater than it from the non-increasing list
        # otherwise sort the whole list and return ie skip this step
        if decreasing_ix != -1:

            # add the decreasing element to the occurrences map
            occurrences[nums[decreasing_ix]] += 1

            # remove the first element in the occurrences map that is greater than the decreasing element
            for i in range(nums[decreasing_ix] + 1, 101):
                if occurrences[i] > 0:
                    occurrences[i] -= 1
                    # set the decreasing element to the element we just removed
                    nums[decreasing_ix] = i
                    break

        # overwrite the non-increasing part of the list with the occurrences map
        ix = decreasing_ix + 1
        for i in range(101):
            for j in range(occurrences[i]):
                nums[ix] = i
                ix += 1


nums = [1, 1, 5, 2, 0, 0]
nums = [1, 2, 3]
nums = [3, 2, 1]
s = Solution()
s.nextPermutation(nums)
print(nums)
