from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        for_deletion = -11111
        for_deletion_count = 0
        most_recent = nums[1]
        # nums list is in non-decreasing order
        # overwrite every element but the first two of each value with special for_deletion value
        for ix in range(2, len(nums)):
            last_two_values_are_same_as_current = nums[ix] == nums[ix - 1] == nums[ix - 2]
            current_is_same_as_2nd_previous_and_prev_is_deleted = nums[ix] == nums[ix - 2] and \
                                                                  nums[ix - 1] == for_deletion
            current_is_same_as_most_recent_and_1st_2nd_previous_are_deleted = nums[ix] == most_recent and \
                                                                              nums[ix - 1] == for_deletion and \
                                                                              nums[ix - 2] == for_deletion
            if last_two_values_are_same_as_current or \
                    current_is_same_as_2nd_previous_and_prev_is_deleted or \
                    current_is_same_as_most_recent_and_1st_2nd_previous_are_deleted:
                nums[ix] = for_deletion
                for_deletion_count += 1
            else:
                most_recent = nums[ix]

        # move every element to the left number of times equal to total number of elements marked for deletion so far
        move_ix = 0
        for ix in range(2, len(nums)):
            if nums[ix] == for_deletion:
                move_ix += 1
            else:
                nums[ix - move_ix] = nums[ix]

        return len(nums) - for_deletion_count


nums = [1, 1, 1, 1, 1, 2, 2, 3]
nums = [1, 1]
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)
